from google.cloud import storage
from pathlib import Path
import json


def download_json(content, dir, filename):
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
            print(f"{filename} already exists")
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
