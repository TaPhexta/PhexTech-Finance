from decimal import Decimal
from database import load_data, save_data
from datetime import datetime

def deposit_funds(username, amount_str):
    """
    Business logic; updates the JSON with new balance and history
    """
    data = load_data()
    
    # 1. convert str to decimal for accurate financial calculations
    current_balance = Decimal(data[username]['balance'])
    deposit_amount = Decimal(amount_str)
    
    # 2. calculate new balance
    new_balance = current_balance + deposit_amount
    
    # 3. update user data
    data[username]['balance'] = str(new_balance)  # Store as string to maintain JSON compatibility
    
    # 4. record the actual transaction for history
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    history_entry = f"{timestamp} | Deposit: R{deposit_amount} | New Balance: R{new_balance}"
    data[username]['history'].append(history_entry)
    
    # 5. Save to JSON
    save_data(data)
    return True, f"Successfully deposited R{deposit_amount}. Your new balance is R{new_balance}."
    
def withdraw_funds(username, amount_str):
    """
    Business Logic; checks for sufficient funds and updates JSON with new balance and history
    after succesful withdrawal
    """
    data = load_data()
    
    current_balance = Decimal(data[username]['balance'])
    withdraw_amount = Decimal(amount_str)
    
    # 1. Check for sufficient funds
    if withdraw_amount > current_balance:
        return False, "Insufficient funds. Transaction cancelled."
    
    # 2. Calculation
    new_balance = current_balance - withdraw_amount
    
    # 3. Update user data
    data[username]['balance'] = str(new_balance) 
    
    # 4. Record transaction for history
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    history_entry = f"{timestamp} | Withdraw: R{withdraw_amount} | New Balance: R{new_balance}"
    data[username]['history'].append(history_entry)
    
    save_data(data)
    return True, f"Successfully withdraw R{withdraw_amount}"    
    
    