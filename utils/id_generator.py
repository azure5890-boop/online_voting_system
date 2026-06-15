import random

def national_id_generator():
    try:
        full_name = input("Enter Your Full Name: ")
        dob = input("Enter Your Date of Birth (YYYY-MM-DD): ")
        phone_number = input("Enter Your Phone Number: ")
        gender = input("Enter Your Gender (M/F): ").upper()
        if gender not in ["M", "F"]:
            print("Invalid Gender")
            return None
        national_id = f"IND-{dob[:4]}-{phone_number[-4:]}"
        return national_id
    except Exception as e:
        print("An error occurred during ID generation:", e)
        return None
    