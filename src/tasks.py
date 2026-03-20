import json
import os

# Defining database file name
DATA_FILE = 'tasks.json'

def load_data() -> list:
    """Load data from the database."""
    if not os.path.exists(DATA_FILE):
        return {}
    
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}
    
def save_data(data: dict) -> None:
    """Save data to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)
        
def generate_username(first_name: str, last_name: str) -> list:
    """Generate a username based on the first and last name."""
    f = first_name.lower().strip()
    l = last_name.lower().strip()
    
    opt1 = f"{l}{f}"              #SurnameName
    opt2 = f"{f}{l[:4]}"          #NameSurn (first 4 letters of surname)
    return [opt1, opt2]

def is_valid_pin(pin: str) -> bool:
    """Check for 6 digits with no more than 3 repeating numbers"""
    if not pin.isdigit() or len(pin) != 6:
        return False
    
    # check if any single digit appears more than 3 times
    for digit in set(pin):
        if pin.count(digit) > 3:
            return False
    return True
    
def create_profile(username: str, pin: str) -> None:
    """Create a new user profile."""
    data = load_data()
    data[username] = {
        'pin': pin,
        'tasks': []
    }
    save_data(data)
    
def authenticate(username: str, pin: str) -> bool:
    """Authenticate user credentials."""
    data = load_data()
    user_data = data.get(username)
    if user_data and user_data['pin'] == pin:
        return True
    return False

def get_user_tasks(username: str) -> list:
    """Return the task list for specific auth'd user"""
    data = load_data()
    return data.get(username, []).get('tasks', [])

# CRUD operations for tasks
    
def add_task(username: str, description: str, time: str) -> None:
    data = load_data()
    if username in data:
        # Now saving description AND due_time
        data[username]["tasks"].append({
            "description": description, 
            "completed": False,
            "time": time        # now including time at which task is set for
        })
        save_data(data)

def edit_task(username: str, index: int, new_desc: str) -> bool:
    """Edits a specific user's task by index (1-based)."""
    data = load_data()
    try:
        # use index -1 since users see 123
        data[username]["tasks"][index - 1]["description"] = new_desc
        save_data(data)
        return True
    except (KeyError, IndexError):
        return False
    
def delete_task(username: str, index: int) -> bool:
    """Deletes a specific user's task by index (1-based)."""
    data = load_data()
    try:
        # use index -1 since users see 123
        data[username]["tasks"].pop(index - 1)
        save_data(data)
        return True
    except (KeyError, IndexError):
        return False
    
def toggle_task(username: str, index: int) -> bool:
    """Flips the completed status for a specific user's task."""
    data = load_data()
    try:
        # use index -1 since users see 123
        current_status = data[username]["tasks"][index - 1]["completed"]
        data[username]["tasks"][index - 1]["completed"] = not current_status
        save_data(data)
        return True
    except (KeyError, IndexError):
        return False
