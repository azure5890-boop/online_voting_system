from citizen.citizen_register import register_citizen
from utils.id_generator import national_id_generator
from voter.voter_register import voter_register
from voter.voter_login import voter_login
from candidate.candidate_register import register_candidate
from admin.admin_login import admin_login
from candidate.candidate_status import candidate_status

def display_menu():
    print("\n--- Voting Menu ---\n")
    print("1. Citizen Registration")
    print("2. Voter Registration")
    print("3. Candidate Registration")
    print("4. Voter Login")
    print("5. Admin Login")

def main():
    print("+--------------------------------------+")
    print("| Welcome to the Online Voting System! |")
    print("+--------------------------------------+")
    while True:
        display_menu()
        try:
            choice = input("\nEnter your choice: ")
            if choice == "1":
                ch = input("Do You Have National ID? (yes/no): ")
                if ch.lower() in ["yes", "y"]:
                    register_citizen()
                elif ch.lower() in ["no", "n"]:
                    print("\nGenerating National ID...")
                    print("\nYour National ID:", national_id_generator())
                    register_citizen()
                else:
                    print("Please enter yes/y or no/n.")
            elif choice == "2":
                voter_register()
            elif choice == "3":
                print("\n1. Candidate Registration")
                print("2. Show Candidate Status\n")
                ch_1 = input("Enter choice: ")
                if ch_1 == "1":
                    register_candidate()
                elif ch_1 == "2":
                    candidate_status()
                elif ch_1 == "3":
                    print("\nExisting.....")
                    break 
            elif choice == "4":
                voter_login()
            elif choice == "5":
                admin_login()
            else:
                print("\nInvalid Choice")
        except Exception as e:
            print("An error occurred:", e)
main()
