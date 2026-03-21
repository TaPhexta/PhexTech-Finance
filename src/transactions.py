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
    
def transfer_funds(sender_username, recipient_acc_no, amount_str):
    """
    Business Logic; checks for sufficient funds, verifies recipient, and updates JSON with new balances and history
    after successful transfer
    """
    data = load_data()
    amount = Decimal(amount_str)
    
    # check if sender has sufficient funds
    sender_bal = Decimal(data[sender_username]['balance'])
    if amount > sender_bal:
        return False, "Insufficient funds. Transfer cancelled."
    
    # find recipient by account number
    recipient_username = None
    for username, details in data.items():
        if details.get('account_no') == recipient_acc_no:
            recipient_username = username
            break
        
    if not recipient_username:
        return False, "Recipient account not found. Transfer cancelled."
    
    if recipient_username == sender_username:
        return False, "Cannot transfer to the same account. Transfer cancelled."
    
    # Perform transfer
    data[sender_username]['balance'] = str(sender_bal - amount)
    # add to recipient's balance
    recipient_bal = Decimal(data[recipient_username]['balance'])
    data[recipient_username]['balance'] = str(recipient_bal + amount)
    
    # history entries for both
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    data[sender_username]['history'].append(
        f"{timestamp} | Transfer Sent: -R{amount} to {recipient_username} (Acc No: {recipient_acc_no}) | New Balance: R{data[sender_username]['balance']}"
    )
    data[recipient_username]['history'].append(
        f"{timestamp} | Transfer Received: +R{amount} from {sender_username} (Acc No: {data[sender_username]['account_no']}) | New Balance: R{data[recipient_username]['balance']}"
    )
    
    # save
    save_data(data)
    return True, f"Successfully transferred R{amount} to {recipient_username}."