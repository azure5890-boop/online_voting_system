from database.db_connect import connection_db

def view_pending_candidates():
    connection = None
    cursor = None
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

def view_approved_candidates():
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            SELECT candidate_id, national_id, party_name, position, status FROM candidates WHERE status = 'Approved'
            """
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def view_rejected_candidates():
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            SELECT candidate_id, national_id, party_name, position, status FROM candidates WHERE status = 'Rejected'
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
    candidate_id = input("Enter Candidate ID Approve: ")
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            UPDATE 
            SET status = 'Approved'
            WHERE candidate_id = %s
            """
        cursor.execute(query,(candidate_id,))
        connection.commit()
        if cursor.rowcount > 0 :
            print("\nCandidate Approved Successfully!")
        else:
            print("\nCandidate not found.")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            
def reject_candidate():
    candidate_id = input("Enter Candidate ID to Reject: ")
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            UPDATE
            SET status = 'Rejected'
            WHERE status = 'Pending'
        """
        cursor.execute(query,(candidate_id,))
        connection.commit()
        if cursor.rowcount > 0:
            print("\nCandidate Rejected Successfully!")
        else:
            print("\nCandidate not found.")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
