import maskpass
from account import register_user, load_data

def clear_screen():
    """Keep the console screen clean."""
    print("\n" * 20)
    
def main_menu():
    while True:
        print("--- Welcome to PhexTech-Finance ---")
        print("1. Create New Account")
        print("2. Login")
        print("3. Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            username = input("Choose a username:  ")
            
            # security first: 6 digit pin with masking
            pin = maskpass.askpass("Choose a 5-digit PIN: ", mask="*")
            
            if not pin.isdigit() or len(pin) != 5:
                print("PIN must be exactly 5 digits.")
                continue
            
            success, message = register_user(username, pin)
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