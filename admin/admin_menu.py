from database.db_connect import connection_db
from admin.approve_candidate import (
    view_pending_candidates,
    approve_candidate,
    reject_candidate
)

def super_admin_menu():
    while True:
        print("\n--- Super Admin Menu ---\n")
        print("1. View Pending Candidate")
        print("2. Approve Candidate")
        print("3. Reject candidate")
        print("4. View Results")
        print("5. Logout")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            candidates = view_pending_candidates()
            if not candidates:
                print("\nNo Pending Candidate.")
            else:
                for candidate_id, national_id, party_name, position, status in candidates:
                    print("\n--- Pending Candidates ---\n")
                    print(f"Candidate ID : {candidate_id}")
                    print(f"National ID : {national_id}")
                    print(f"Party Name : {party_name}")
                    print(f"Position : {position}")
                    print(f"Status : {status}")
                    print("+------------------------------+\n")
        elif choice == "2":
            approve_candidate()
        elif choice == "2":
            reject_candidate()
        

