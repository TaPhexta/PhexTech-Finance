import maskpass
from database import load_data

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

def show_profile(user):
    """Displays the user's profile information."""
    print(f"\n--- PROFILE FOR {user['username'].upper()} ---")
    print(f"Full Name: {user['first_name']} {user['last_name']}")
    print(f"ID Number: {user['id_no']}")
    print(f"Email:     {user['email']}")
    print(f"Phone:     {user['phone']}")
    print(f"Address:   {user['address']}")
    
    