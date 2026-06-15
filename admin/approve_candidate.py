from database.db_connect import connection_db

def view_pending_candidates():
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            SELECT candidate_id, national_id, party_name, position, status FROM candidates WHERE status = 'Pending'
            """
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def approve_candidate():
    try:
        connection = connection_db()
        cursor = connection.cursor()
