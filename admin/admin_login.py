from utils.validators import verify_admin_login
from admin.admin_menu import(
    super_admin_menu,
    candidate_admin_menu,
    result_admin_menu
)

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
        print("\nLogin Successful!")
        print(f"\nWelcome {username}!")
        print(f"Role: {role}\n")
        if role == "super_admin":
            super_admin_menu()
        elif role == "candidate_admin":
            candidate_admin_menu()
        elif role == "result_admin":
            result_admin_menu()
        else:
            print("\nInvalid admin role.")
    except Exception as e:
        print("An error occur during login:",e)


        