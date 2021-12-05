import os
from datetime import datetime
import json
from dotenv import load_dotenv
from app.service import azure_client, singlestore_client

load_dotenv()

BACKUP_CONTAINER = "seismos-singlestore-backup"
BACKUPS_AMOUNT = 4
AZURE_CREDENTIALS = json.dumps({
    "account_name": os.environ.get("AZURE_ACCOUNT_NAME"),
    "account_key": os.environ.get("AZURE_ACCOUNT_KEY"),
})
CREDENTIALS_SUFFIX = "\nCREDENTIALS '" + AZURE_CREDENTIALS + "';"


class BackupBaseController():
    def get_backup_data(self):
        # Get all backups files
        blobs = azure_client.get_files(BACKUP_CONTAINER)
        backups_raw = set()
        for blob in blobs:
            backup_timestamp = blob[:blob.index("/")]
            backups_raw.add(backup_timestamp)

        backups = [float(timestamp) for timestamp in backups_raw]
        backups.sort()
        return blobs, backups

    def backup(self):
        if singlestore_client.is_db_empty("seismos"):
            print("base empty :(")
            return None

        print("Make backup")

        def exec_backup(cursor):
            sql = f"BACKUP DATABASE seismos TO Azure '{BACKUP_CONTAINER}/{datetime.now().timestamp()}'" + CREDENTIALS_SUFFIX
            cursor.execute(sql)
            cursor.fetchone()

            # Get all backups files
            blobs, backups = self.get_backup_data()
            # Remove old backups
            backups_remove_amount = len(backups) - BACKUPS_AMOUNT
            backups_remove_amount = 0 if backups_remove_amount < 0 else backups_remove_amount

            backups_to_remove = backups[-backups_remove_amount:] if backups_remove_amount else []

            for i, backup_prefix in enumerate(backups_to_remove):
                backups_to_remove[i] = str(backup_prefix)

            for blob_file in blobs:
                if any(blob_file.startswith(remove_prefix) for remove_prefix in backups_to_remove):
                    azure_client.delete_blob(BACKUP_CONTAINER, blob_file)

        singlestore_client.execute_cursor(exec_backup)

    def restore(self, last_backup):
        _, backups = self.get_backup_data()
        if len(backups) <= last_backup:
            return f"Backup with {last_backup} index not created"

        def exec_restore(cursor):
            latest_backup = backups[0]
            backup_path = f"{str(latest_backup)}/seismos.backup"
            sql = "DROP DATABASE seismos;"
            cursor.execute(sql)
            cursor.fetchone()
            sql = f"\nRESTORE DATABASE seismos FROM Azure '{BACKUP_CONTAINER}/{backup_path}'{CREDENTIALS_SUFFIX}"
            cursor.execute(sql)
            cursor.fetchone()

        singlestore_client.execute_cursor(exec_restore)
