from database.db_connect import connection_db
from admin.approve_candidate import view_approved_candidates
from utils.validators import (
    check_has_voted,
    check_candidate_id
)

def show_approved_candidate():
    candidates = view_approved_candidates()
    if not candidates:
        print("\nNo Approved Candidate.")
    else:
        print("\n--- Approved Candidates ---\n")
        for candidate_id, national_id, party_name, position, status in candidates:
            print("+------------------------------+")
            print(f"Candidate ID : {candidate_id}")
            print(f"National ID : {national_id}")
            print(f"Party Name : {party_name}")
            print(f"Position : {position}")
            print(f"Status : {status}")
            print("+------------------------------+\n")  
            
def cast_vote(voter_id):
    if check_has_voted(voter_id):
        print("\nYou have already voted.")
        return
    show_approved_candidate()
    try:
        candidate_id = int(input("Enter Candidate ID: "))
    except ValueError:
        print("\nInvalid Candidate ID.")
        return
    if not check_candidate_id(candidate_id):
        print("\nInvalid Candidate ID.")
        return
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()

        query = """
            INSERT INTO votes(
            voter_id,
            candidate_id
            )
            VALUES(%s,%s)
            """
        values = (
            voter_id,
            candidate_id
        )
        cursor.execute(query,values)

        query = """
            UPDATE candidates
            SET vote_count = vote_count + 1
            WHERE candidate_id = %s
            """
        cursor.execute(query,(candidate_id,))

        query = """
            UPDATE voters
            SET has_voted = True
            WHERE voter_id = %s
            """
        cursor.execute(query,(voter_id,))

        connection.commit()
        print("\nVote Cast Successfully!")

    except Exception as e:
        connection.rollback()
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
