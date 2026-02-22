from connect import get_db_connection

def create_users_table():
    """Create the users table if it doesn't exist."""
    
    create_table_query = """
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='users' AND xtype='U')
    CREATE TABLE users (
        account_id INT IDENTITY(1,1) PRIMARY KEY,
        username NVARCHAR(50) UNIQUE NOT NULL,
        password_hash NVARCHAR(255) NOT NULL,
        email NVARCHAR(100) UNIQUE NOT NULL,
        first_name NVARCHAR(50),
        last_name NVARCHAR(50),
        phone_number NVARCHAR(20),
        date_of_birth DATE,
        gender NVARCHAR(10),
        street_address NVARCHAR(255),
        city NVARCHAR(100),
        state NVARCHAR(50),
        zip_code NVARCHAR(20),
        country NVARCHAR(50) DEFAULT 'USA',
        is_active BIT DEFAULT 1,
        created_at DATETIME DEFAULT GETDATE(),
        updated_at DATETIME DEFAULT GETDATE()
    )
    """
    
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(create_table_query)
            conn.commit()
            print("Users table created successfully or already exists.")
    except Exception as e:
        print(f"Error creating users table: {e}")

if __name__ == "__main__":
    create_users_table()
