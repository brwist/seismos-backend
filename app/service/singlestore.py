import os
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()

BACKUP_CONTAINER = "seismos-singlestore-backup"
BACKUPS_AMOUNT = 4
DB_USER = os.environ.get("DB_USER", "root")
DB_PASS = os.environ.get("DB_PASSWORD", "")
DB_NAME = os.environ.get("DB_NAME", "")
DB_PORT = int(os.environ.get("DB_PORT"))


class SinglestoreClient():
    def create_connection(self):
        connection = pymysql.connect(
            host='localhost', port=DB_PORT,
            user=DB_USER, password=DB_PASS, database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )

        return connection

    def execute_cursor(self, exec_callback):
        with self.create_connection() as connection:
            with connection.cursor() as cursor:
                return exec_callback(cursor)

    def is_db_empty(self, db_name):
        def check_is_db_exists(cursor):
            cursor.execute("SHOW DATABASES;")
            if not any(db["Database"] == db_name for db in cursor._rows):
                return True

            cursor.execute("SHOW TABLES;")
            if not len(cursor._rows):
                return True

            for tablename in ("user", "project"):
                cursor.execute(f"SELECT * FROM {tablename};")
                if not len(cursor._rows):
                    return True

            return False

        return self.execute_cursor(check_is_db_exists)

    def is_db_exists(self, db_name):
        def callback(cursor):
            cursor.execute("SHOW DATABASES;")
            if not any(db["Database"] == db_name for db in cursor._rows):
                return False
            return True

        return self.execute_cursor(callback)
