import maskpass
from account import authenticate_user, register_user, load_data, load_data, save_data, hash_pin

def clear_screen():
    """Keep the console screen clean."""
    print("\n" * 10)
    
    from account import load_data, register_user, hash_pin

def get_registration_input():
    print("\n--- NEW ACCOUNT ENROLLMENT ---")
    
    # 1. Unique Username Logic (Reused from previous app)
    data = load_data()
    while True:
        username = input("Choose Username: ").lower().strip()
        if not username.isalnum():
            print("Error: Username must be alphanumeric (letters and numbers only).")
            continue
        if username in data:
            print(f"Error: The username '{username}' is already taken. Please try another.")
            continue
        break

    # 2. Personal Details
    first_name = input("First Name: ").strip().capitalize()
    last_name = input("Surname: ").strip().capitalize()
    email = input("Email: ").strip()
    phone = input("Cell Number: ").strip()
    id_no = input("ID Number: ").strip()
    address = input("Home Address: ").strip()
    
    # 3. PIN Validation (6-digit check)
    while True:
        pin = maskpass.askpass(prompt="Create 6-digit PIN: ", mask="*")
        if len(pin) == 6 and pin.isdigit():
            break
        print("Error: PIN must be exactly 6 digits.")

    # 4. Mandatory Initial Deposit (R10 Minimum)
    while True:
        try:
            deposit = float(input("Initial Deposit (Min R10.00): "))
            if deposit >= 10.00:
                break
            print("Error: Minimum deposit is R10.00.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value (e.g., 50.00).")

    # Final Dictionary Package
    return {
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "id_no": id_no,
        "address": address,
        "pin": pin, # This gets hashed inside account.register_user
        "balance": str(deposit)
    }
        
def login():
    username = input("Username: ").lower().strip()
    pin = maskpass.askpass("PIN: ", mask="*")
    
    data = load_data()
    
    #check if username exists and pin matches
    if username in data and data[username]["pin"] == hash_pin(pin):
        print(f"Welcome back, {data[username]['first_name']}!")
        return username
    else:
        print("\nInvalid username or PIN.")
        return None
    
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
        
        if choice == "1":
            print("\n[Deposit Feature Coming Soon]") 
        elif choice == "2":
            print("\n[Withdraw Feature Coming Soon]")
        elif choice == "3":
            print(f"\n--- Transaction History ---")
            for record in current_user.get('history', []):
                print(f" > {record}")
        elif choice == "4":
            print(f"\n--- Profile Info ---")
            print(f"Email: {current_user['email']}")
            print(f"Phone: {current_user['phone']}")
            print(f"ID No: {current_user['id_no']}")
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
            user_details = get_registration_input()
            success, message = register_user(user_details)
            print(message)
            
        elif choice == '2':
            # "Login logic coming in next update!"
            print("Login functionality is under development. Please check back later.")
            
        elif choice == '3':
            print("Thank you for using PhexTech-Finance. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            
if __name__ == "__main__":
    clear_screen()
    main_menu()