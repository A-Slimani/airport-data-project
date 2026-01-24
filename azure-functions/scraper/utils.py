from azure.storage.filedatalake import DataLakeServiceClient, ContentSettings
from azure.identity import DefaultAzureCredential
from google.cloud import storage
from pathlib import Path
import json


def download_file(content, dir, filename):
    dir_path = Path(dir)

    if not dir_path.is_dir():
        dir_path.mkdir(exist_ok=True)

    try:
        filepath = Path(f"{dir}/{filename}")
        if not filepath.exists():
            with open(f"{dir}/{filename}", "w", encoding="utf-8") as f:
                json.dump(content, f, indent=2)
            print(f"{filename} downloaded")
        else:
            print(f"{filename} already exists. Skipping...")
    except Exception as e:
        print(f"Failed to write: {e}")


def upload_blob(content, filename):
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket("raw_flight_data-a53432d2")
        blob = bucket.blob(filename)

        if blob.exists():
            print(f"{filename} already exists in blob. Skipping...")
            return None

        json_data = json.dumps(content, indent=2)
        blob.upload_from_string(json_data, content_type='application/json')

        print(f"blob {filename} uploaded.")
    except Exception as e:
        print(f"Failed to upload to blob storage: {e}")


def upload_blob_az(content, filename, directory):
    try:
        service_client = DataLakeServiceClient(
            "https://airportdataproject.dfs.core.windows.net",
            credential=DefaultAzureCredential()
        )

        file_system_client = service_client.get_file_system_client("airport-data")
        directory_client = file_system_client.get_directory_client(directory)
        file_client = directory_client.get_file_client(filename)

        json_payload = json.dumps(content)
        json_settings = ContentSettings(content_type='application/json')

        file_client.upload_data(json_payload, overwrite=True, content_settings=json_settings)

        print(f"{filename} uploaded to {directory}")
    except Exception as e:
        print(f"Failed to upload to blob storage: {e}")
