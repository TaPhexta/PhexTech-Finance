import maskpass
from auth import register_user, authenticate_user
from database import load_data
from transactions import deposit_funds, withdraw_funds
from utilities import clear_screen
import views
    
def dashboard(user_session):
    """The 'Logged In' experience."""
    username = user_session['username']
    
    while True:
        # Reload data to ensure balance/history is always current
        data = load_data()
        current_user = data[username]
        
        print("\n================================")
        print(f"       PHEXTECH DASHBOARD       ")
        print(f"  Welcome, {current_user['first_name']} {current_user['last_name']}")
        print(f"  Cheque Account Balance: R{current_user['balance']}")
        print("================================")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Account & History")
        print("4. Profile Details")
        print("5. Logout")
        
        choice = input("\nSelect an option: ")
        
        # DEPOSIT
        if choice == "1": 
            # 1. Ask for the amount (views)
            amount_to_add = views.get_deposit_amount()
            
            # 2. Process the transaction
            success, message = deposit_funds(username, amount_to_add) 
            
            # 3. Show the result
            print(f"\n[SYSTEM]: {message}")
            
        # WITHDRAW
        elif choice == "2":
            # 1. Ask for the amount (views)
            amount_to_remove = views.get_withdrawal_amount()
            
            # 2. Process the transaction
            success, message = withdraw_funds(username, amount_to_remove)
            
            # 3. Show the result
            if success:
                print(f"\n[SYSTEM]: {message}")
            else:
                print(f"\n[SYSTEM]: {message}")
                
        # HISTORY & ACCOUNT DETAILS
        elif choice == "3":
            views.show_history(current_user)
                
        # PROFILE DETAILS
        elif choice == "4":
                views.show_profile(current_user)
                
        # LOGOUT
        elif choice == "5":
            print(f"Logging out {username}... See you soon!")
            break
        else:
            print("Invalid choice.")
            
def login_flow():
    """
    Handles the login attempt and starts the session if successful.
    """
    print("\n--- LOGIN TO YOUR ACCOUNT ---")
    username = input("Username: ").lower().strip()
    pin = maskpass.askpass("PIN: ", mask="*")
    
    user_data = authenticate_user(username, pin)
    
    if user_data:
        dashboard(user_data)
    else:
        print("\nAccess Denied: Incorrect username or PIN.")

def main_menu():
    while True:
        print("--- Welcome to PhexTech-Finance ---")
        print("1. Create New Account")
        print("2. Login")
        print("3. Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            user_details = views.get_registration_input()
            success, message = register_user(user_details)
            print(message)
            
        elif choice == '2':
            login_flow()
            
        elif choice == '3':
            print("Thank you for using PhexTech-Finance. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            
if __name__ == "__main__":
    clear_screen()
    main_menu()