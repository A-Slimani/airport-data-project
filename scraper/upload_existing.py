from utils.file_utils import get_json_files 
from utils.db_utils import upload_to_db


data = get_json_files('../data')
upload_to_db(data)