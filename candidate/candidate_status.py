from database.db_connect import connection_db
from utils.validators import check_candidate_exists

def candidate_status():
    print("\n--- Candidate Status ---\n")
    national_id = input("Enter National ID: ")
    if not check_candidate_exists(national_id):
        print("\nCandidate not found.")
        return
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            SELECT status FROM candidates WHERE national_id = %s
        """
        cursor.execute(query,(national_id,))
        results = cursor.fetchone()
        if results:
            print(f"\nCandidate Status: {results[0]}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
