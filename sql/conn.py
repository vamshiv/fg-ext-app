import os
os.add_dll_directory(r'C:\IBM\DB2\clidriver\bin')
import ibm_db
from config import DB_CONFIG

def get_db_connection():
    conn_str = (
        f"DATABASE={DB_CONFIG['database']};"
        f"HOSTNAME={DB_CONFIG['host']};"
        f"PORT={DB_CONFIG['port']};"
        f"PROTOCOL=TCPIP;"
        f"UID={DB_CONFIG['user']};"
        f"PWD={DB_CONFIG['password']};"
    )
    conn = ibm_db.connect(conn_str, "", "")
    return conn
