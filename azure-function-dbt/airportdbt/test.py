import pandas as pd
import duckdb


conn = duckdb.connect(':memory:')
conn.execute("INSTALL azure")
conn.execute("INSTALL httpfs")
conn.execute("LOAD azure")
conn.execute("LOAD httpfs")
conn.execute("SET azure_transport_option_type = 'curl';")
conn.execute("""
CREATE SECRET secret (
  TYPE azure,
  PROVIDER credential_chain,
  CHAIN 'cli;env',
  ACCOUNT_NAME 'airportdataproject'
);
""")


df = conn.execute(f"""
SELECT * 
FROM read_json_auto(
    'az://airport-data/RAW/SYD/*.json'
)
""").df()

print(df.head())
