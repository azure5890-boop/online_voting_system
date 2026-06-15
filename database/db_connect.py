import mysql.connector

def connection_db():
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'azure',
            database = 'election_system'
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    return connection
