from database.db_connect import connection_db

def start_election():
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            UPDATE election_status
            SET status = 'Started'
            WHERE election_id = 1
            """
        cursor.execute(query)
        connection.commit()
        print("\nElection started successfully!")
    except Exception as e:
        print(f"An error occure: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def end_election():
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            UPDATE election_status
            SET status = 'Ended'
            WHERE election_id = 1
            """
        cursor.execute(query)
        connection.commit()
        print("\nElection ended successfully!")
    except Exception as e:
        print(f"An error occure: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
