import hashlib
import random
from database import load_data, save_data  

def hash_pin(pin):
    """Hashes the PIN using SHA-256 for secure storage."""
    return hashlib.sha256(pin.encode()).hexdigest()

def register_user(user_details):
    """
    Registers a new user using the user_details dictionary.
    Checks for existence, hashes the PIN, and saves to the JSON database.
    """
    # Load current database
    data = load_data()
    
    # Extract username from the passed dictionary
    username = user_details['username']
    
    # Check if the account already exists
    if username in data:
        return False, "Error: Username already exists."
    
    # Hash the PIN inside the dictionary for security
    # This ensures '123456' becomes a non-reversible hash string
    user_details['pin'] = hash_pin(user_details['pin'])
    
    # Initialize the transaction history with the mandatory R10+ deposit
    user_details['history'] = [f"Initial Deposit: R{user_details['balance']}"]
    
    # Generate a unique account number
    user_details['account_no'] = generate_account_number()
    
    # Add this user's dictionary to our main data object
    data[username] = user_details
    
    # Write the updated dictionary back to the JSON file
    save_data(data)
    
    msg = f"Congratulations {user_details['first_name']}, your account was created successfully!"
    return True, msg

def generate_account_number():
    """Generates a unique 10-digit account number."""
    data = load_data()
    # Create a set of all existing account numbers for quick lookup
    existing_numbers = {details.get('account_no') for details in data.values()}
    
    while True:
        # Generate a random 10-digit number as a string
        new_no = str(random.randint(1000000000, 9999999999))
        if new_no not in existing_numbers:
            return new_no

def authenticate_user(username, entered_pin):
    """
    Checks if the provided username and PIN are valid for login.
    Returns user data if valid, else nothing otherwise. 
    """
    data = load_data()
    username = username.lower().strip()
    
    if username in data:
        # Hash the provided PIN and compare with stored hash
        if data[username]['pin'] == hash_pin(entered_pin):
            return data[username]
    return None