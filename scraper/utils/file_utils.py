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
    print(f"failed to write: {e}")


def get_json_files(path):
  folder = Path(path)
  json_files = folder.glob('*.json')

  data = []

  for json_file in json_files:
    with open(json_file, 'r') as f:
      data.append((json_file.stem, json.load(f)))
  
  return data
