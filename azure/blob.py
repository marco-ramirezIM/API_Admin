from typing import BinaryIO
from azure.storage.blob import BlobServiceClient
from config.setup import Settings as settings

blob_service_client = BlobServiceClient.from_connection_string(
    settings.AZURE_BLOB_STORAGE.STRING_CONNECTION
)


def upload_blob(filename: str, container: str, data: BinaryIO):
    blob_client = blob_service_client.get_blob_client(
        container=container, blob=filename
    )

    blob_client.upload_blob(data, overwrite=True)
    return blob_client.url
