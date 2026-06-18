from admin.approve_candidate import (
    approve_candidate,
    reject_candidate,
    view_pending_candidates,
    view_approved_candidates,
    view_rejected_candidates
)

from admin.results import view_results

def super_admin_menu():
    while True:
        print("\n--- Super Admin Menu ---\n")
        print("1. Approve Candidate")
        print("2. Reject candidate")
        print("3. View Pending Candidate")
        print("4. View Approved Candidate")
        print("5. View Rejected Candidate")
        print("6. View Results")
        print("7. Logout")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            approve_candidate()
        elif choice == "2":
            reject_candidate()
        elif choice == "3":
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
        elif choice == "4":
            candidates = view_approved_candidates()
            if not candidates:
                print("\nNo Approved Candidate.")
            else:
                for candidate_id, national_id, party_name, position, status in candidates:
                    print("\n--- Approved Candidates ---\n")
                    print(f"Candidate ID : {candidate_id}")
                    print(f"National ID : {national_id}")
                    print(f"Party Name : {party_name}")
                    print(f"Position : {position}")
                    print(f"Status : {status}")
                    print("+------------------------------+\n")
        elif choice == "5":
            candidates = view_rejected_candidates()
            if not candidates:
                print("\nNo Rejected Candidate.")
            else:
                for candidate_id, national_id, party_name, position, status in candidates:
                    print("\n--- Rejected Candidates ---\n")
                    print(f"Candidate ID : {candidate_id}")
                    print(f"National ID : {national_id}")
                    print(f"Party Name : {party_name}")
                    print(f"Position : {position}")
                    print(f"Status : {status}")
                    print("+------------------------------+\n")
        elif choice == "6":
            view_results()
        elif choice == "7":
            print("\n Logging out.....")
            break
        else:
            print("\nInvalid choice.")

def candidate_admin_menu():
    while True:
        print("\n--- Candidate Admin Menu ---\n")
        print("1. Approve Candidate")
        print("2. Reject candidate")
        print("3. View Pending Candidate")
        print("4. View Approved Candidate")
        print("5. View Rejected Candidate")
        print("6. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            approve_candidate()
        elif choice == "2":
            reject_candidate()
        elif choice == "3":
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
        elif choice == "4":
            candidates = view_approved_candidates()
            if not candidates:
                print("\nNo Approved Candidate.")
            else:
                for candidate_id, national_id, party_name, position, status in candidates:
                    print("\n--- Approved Candidates ---\n")
                    print(f"Candidate ID : {candidate_id}")
                    print(f"National ID : {national_id}")
                    print(f"Party Name : {party_name}")
                    print(f"Position : {position}")
                    print(f"Status : {status}")
                    print("+------------------------------+\n")
        elif choice == "5":
            candidates = view_rejected_candidates()
            if not candidates:
                print("\nNo Rejected Candidate.")
            else:
                for candidate_id, national_id, party_name, position, status in candidates:
                    print("\n--- Rejected Candidates ---\n")
                    print(f"Candidate ID : {candidate_id}")
                    print(f"National ID : {national_id}")
                    print(f"Party Name : {party_name}")
                    print(f"Position : {position}")
                    print(f"Status : {status}")
                    print("+------------------------------+\n")
        else:
            print("\nInvalid choice.")

def result_admin_menu():
    while True:
        print("\n--- Result Admin Menu ---\n")
        print("1. View Results")
        print("2. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            view_results()
        elif choice == "2":
            print("\n Logging out.....")
            break
        else:
            print("\nInvalid choice.")
            