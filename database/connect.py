import pyodbc
from contextlib import contextmanager
import os
from dotenv import load_dotenv

load_dotenv()

connection_string = f"Driver={{ODBC Driver 18 for SQL Server}};Server=tcp:{os.getenv('DB_SERVER')},1433;Database={os.getenv('DB_NAME')};Uid={os.getenv('DB_USER')};Pwd={os.getenv('DB_PASSWORD')};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"


@contextmanager
def get_db_connection():
    """Context manager for database connections."""
    conn = None
    try:
        conn = pyodbc.connect(connection_string)
        yield conn
    finally:
        if conn:
            conn.close()

# Test the connection when run directly
if __name__ == "__main__":
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            if cursor is not None:
                print("Connected!")
            else:
                print("Not Connected")
    except Exception as e:
        print(f"Connection failed: {e}")