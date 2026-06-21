from database.db_connect import connection_db
from utils.validators import (
    check_phone_number_exists,
    check_national_id_exists
)

def register_citizen():
    print("\n--- Citizen Registration ---\n")
    full_name = input("Enter Your Full Name: ").title()
    dob = input("Enter Your Date of Birth (YYYY-MM-DD): ")
    phone_number = input("Enter Your Phone Number: ")
    gender = input("Enter Your Gender (M/F): ").upper()
    national_id = input("Enter Your National ID: ")
    phone_number.isdigit()
    len(phone_number) == 10
    if gender not in ["M", "F"]:
        print("Invalid Gender")
        return
    connection = None
    cursor = None
    try:
        connection = connection_db()
        cursor = connection.cursor()
        if check_phone_number_exists(phone_number):
            print("\nPhone Number Already Exists. Please Try Again.")
            return
        if check_national_id_exists(national_id):
             print("National ID Already Exists.")
             return
        query = """
            INSERT INTO citizens(
                full_name,
                dob,
                phone_number,
                gender,
                national_id
            ) 
            VALUES (%s, %s, %s, %s, %s)
            """
        values = (
            full_name,
            dob,
            phone_number,
            gender,
            national_id
        )
        cursor.execute(query, values)
        connection.commit()
        print("\nCitizen registered successfully!")
    except Exception as e:
        print("An error occurred during registration:", e)
    finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

