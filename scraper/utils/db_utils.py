from psycopg.types.json import Jsonb
from dotenv import load_dotenv
import psycopg
import os

load_dotenv()

DB_URI = os.getenv('DB_URI')

def upload_to_db(data, **kwargs):
  try:
    conn = psycopg.connect(DB_URI)
    cur = conn.cursor()

    table_name = kwargs.get('table_name')

    cur.execute(f"""
      CREATE TABLE IF NOT EXISTS {table_name} (
        id            SERIAL      PRIMARY KEY,
        name          TEXT        UNIQUE NOT NULL,
        data          JSONB       NOT NULL,
        scraped_at    TIMESTAMP   WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL    
      );
    """)

    terminal_type = kwargs.get('terminal_type')
    flight_type = kwargs.get('flight_type')
    date = kwargs.get('date')

    if terminal_type and flight_type:
      name = f"{date}-{terminal_type}-{flight_type}"
    else:
      name = date 

    insert_query = f"""
      INSERT INTO {table_name} (name, data, scraped_at) 
      VALUES (%s, %s, CURRENT_TIMESTAMP) 
      ON CONFLICT (name) DO UPDATE
      SET 
        data          = EXCLUDED.data,  
        scraped_at    = CURRENT_TIMESTAMP
    """ 

    if isinstance(data, list):
      cur.executemany(insert_query, [(name, Jsonb(record)) for name, record in data])
    else: 
      cur.execute(insert_query, (name, Jsonb(data)))

    conn.commit()
    print(f"record {name} inserted / updated successfully.")
  
  except Exception as e:
    print(f"Error when inserting record into {table_name}: {e}")