import json
import os
from decimal import Decimal

# path logic for finance.json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
DATA_FILE = os.path.join(DATA_DIR, 'finance.json')

STARTING_BALANCE = Decimal('0.01')

def load_data():
    """Fetches the data from the finance.json file."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}
    
def save_data(data):
    """Saves the data to the finance.json file."""
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
        
def register_user(username, pin):
    """Registers a new user with the given username and pin."""
    
    # returns true or false with message depending on user existence
    data = load_data()
    
    if username in data:
        return False, "Username already exists."
    
    # Store Decimal as a string in JSON to prevent precision issues with rounding
    data[username] = {
        'pin': pin,
        'balance': str(STARTING_BALANCE),
        'history': []
    }
    
    save_data(data)
    return True, "User registered successfully."

