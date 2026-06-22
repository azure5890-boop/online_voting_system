from database.db_connect import connection_db

def view_results():
    print("\n--- View Results ---\n")
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            SELECT candidate_id,
                national_id,
                party_name,
                position,
                vote_count
            FROM candidates
            WHERE status = 'Approved'
            ORDER BY vote_count DESC
            """
        cursor.execute(query)
        results = cursor.fetchall()
        if not results:
            print("\nNo approved candidates found.")
            return
        for candidate_id, national_id, party_name, position, vote_count in results:
            print("+----------------------------+")
            print(f"Candidate ID: {candidate_id}")
            print(f"National ID: {national_id}")
            print(f"Party Name: {party_name}")
            print(f"Position: {position}")
            print(f"Vote Count: {vote_count}")
            print("+----------------------------+\n")
    except Exception as e:
        print("Error",e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
