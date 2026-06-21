from voter.cast_vote import cast_vote

def voter_menu(voter_id):
    while True:
        print("\n--- Voter Menu ---\n")
        print("1. Cast Vote")
        print("2. Logout\n")

        choice = input("Enter choice: ")

        if choice == "1":
            cast_vote(voter_id)

        elif choice == "2":
            print("\nLogout successful!")
            break

        else:
            print("\nInvalid choice.")