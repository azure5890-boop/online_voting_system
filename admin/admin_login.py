from database.db_connect import connection_db
from utils.validators import verify_admin_login

def admin_login():
    print("\n--- Admin Login ---\n")
    try:
        connection = connection_db()
        cursor = connection.cursor()
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        result = verify_admin_login(username,password)
        if result is None:
            print("Invalid username or password.")
            return
        role = result[0]
        print(f"\nLogin Successful! Role: {role}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            

        