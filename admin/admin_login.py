from utils.validators import verify_admin_login
from admin.admin_menu import super_admin_menu

def admin_login():
    print("\n--- Admin Login ---\n")
    try:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        result = verify_admin_login(username,password)
        if result is None:
            print("\nInvalid username or password.")
            return
        role = result[0]
        print(f"\nLogin Successful! Role: {role}")
        if role == "super_admin":
            super_admin_menu()
    except Exception as e:
        print("An error occur during login:",e)


        