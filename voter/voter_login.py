from database.db_connect import connection_db
from utils.validators import verify_login
from voter.voter_menu import voter_menu

def voter_login():
    print("\n--- Voter Login ---")
    connection = None
    cursor = None
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        voter_code = input("Enter voter code: ")
        result = verify_login(username,password,voter_code)
        if result is None:
            print("Invalid credentials.")
            return
        connection = connection_db()
        cursor = connection.cursor()
        query = """
            SELECT voter_id , has_voted FROM voters WHERE username = %s
            """
        cursor.execute(query,(username,))
        voter = cursor.fetchone()
        voter_id = voter[0]
        has_voted = voter[1]
        if has_voted:
            print("You have already voted.")
            return
        print("\nLogin Successful!")
        voter_menu(voter_id)
        return voter_id
    except Exception as e:
        print("An error occurred during login:",e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            