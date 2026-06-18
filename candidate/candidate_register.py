from database.db_connect import connection_db
from utils.validators import (
    check_citizen_exists,
    check_age_eligibility,
    check_candidate_exists,
    check_voter_exists
)

def register_candidate():
    print("\n--- Candidate Registration ---\n")
    national_id = input("Enter National ID: ")
    if not check_citizen_exists(national_id):
        print("\nCitizen not found.")
        return
    if not check_age_eligibility(national_id):
        print("\nYou must be at least 18 years old to register as a Candidate.")
        return
    if check_candidate_exists(national_id):
        print("\nCandidate already registered.")
        return
    if check_voter_exists(national_id):
        print("\nVoters can not register as candidate.")
        return
    party_name = input("Enter Party Name: ").title()
    if not party_name.strip():
        print("\nParty name cannot be empty.")
        return
    position = input("Enter Position: ").title()
    try:
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            INSERT INTO candidates(
                national_id,
                party_name,
                position
            )
            VALUES(%s,%s,%s)
            """
        values = (
            national_id,
            party_name,
            position
        )
        cursor.execute(query, values)
        connection.commit()
        print("\n Candidate Registration Successful!")
    except Exception as e:
        print("An error occurred during registration:",e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
