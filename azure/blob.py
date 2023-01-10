from typing import BinaryIO
from azure.storage.blob import BlobServiceClient
from config.setup import Settings as settings
import src.campaigns.exceptions as campaign_exceptions

blob_service_client = BlobServiceClient.from_connection_string(
    settings.AZURE_BLOB_STORAGE.STRING_CONNECTION
)


def upload_blob(filename: str, container: str, data: BinaryIO):
    blob_client = blob_service_client.get_blob_client(
        container=container, blob=filename
    )

    blob_client.upload_blob(data)
    return blob_client.url


def delete_blob(img_name: str):
    try:
        blob_client = blob_service_client.get_blob_client(
            container="imagenes", blob=img_name
        )
        if not blob_client.exists():
            raise campaign_exceptions.blob_does_not_exist_exception(img_name)

        return blob_client.delete_blob()
    except Exception as e:
        raise e
