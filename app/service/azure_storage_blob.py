import os
from pathlib import Path
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError
from dotenv import load_dotenv
from typing import List

load_dotenv()

CONNECT_URL = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_PREFIX = "seismos-"

CONTAINERS = ["hydrophone", "pressure", "pumping_data", "survey", "gamma_ray", "mud_log", "singlestore-backup"]

# add prefix to all containers
for i, container_name in enumerate(CONTAINERS):
    CONTAINERS[i] = CONTAINER_PREFIX + container_name.replace("_", "-")


class AzureClient():
    def __init__(self):
        self.client = BlobServiceClient.from_connection_string(CONNECT_URL)
        self.create_containers()

    def create_containers(self):
        for container_name in CONTAINERS:
            try:
               self.client.create_container(container_name)
            except ResourceExistsError:
                pass

    def upload_file(self, container, filepath):
        container = CONTAINER_PREFIX + container.replace("_", "-")
        if container not in CONTAINERS:
            return None, f"Wrong container: {container}"

        with open(filepath, "rb") as file_data:
            filename = Path(filepath).name
            blob_client = self.client.get_blob_client(container=container, blob=filename)
            blob_client.upload_blob(file_data)

            return True, "File uploaded"

    def get_files(self, container) -> List[str]:
        container_client = self.client.get_container_client(container)
        blob_list = container_client.list_blobs()
        return [blob.name for blob in blob_list]

    def delete_container(self, container):
        self.client.delete_container(container)

    def delete_blob(self, container, blob_name):
        blob_client = self.client.get_blob_client(container=container, blob=blob_name)
        blob_client.delete_blob()
