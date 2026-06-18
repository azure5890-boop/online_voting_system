from database.db_connect import connection_db
from utils.voter_code import voter_code_generator
from utils.validators import (
    check_age_eligibility,
    check_citizen_exists,
    check_voter_exists,
    check_candidate_exists
)
def voter_register():
    print("\n--- Voter Registration ---\n")
    try:
        connection = connection_db()
        cursor = connection.cursor()
        national_id = input("Enter Your National ID: ")
        if not check_age_eligibility(national_id):
            print("\nYou must be at least 18 years old to register as a voter.")
            return 
        print("You are eligible to register as a voter!")
        if not check_citizen_exists(national_id):
            print("Citizen not found. Please register as a citizen first.")
            return 
        
        if check_voter_exists(national_id):
            print("\nYou are already registered as a voter.")
            return
        if check_candidate_exists(national_id):
            print("\nCandidate can not register as a voter.")
            return
        username = input("Create Username: ")
        password = input("Create Password: ")

        voter_code = voter_code_generator()
        print(f"\nYour voter code:- {voter_code}")
        query = """
            INSERT INTO voters(
                national_id,
                username,
                password,
                voter_code
            )
            VALUES (%s,%s,%s,%s)
            """
        values = (
            national_id,
            username,
            password,
            voter_code
        )
        cursor.execute(query, values)
        connection.commit()
    except Exception as e:
        print("An error occurred during registration:", e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
