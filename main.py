from auth import register, login
from messenger import send_message, view_inbox, list_users

def main():
    print("=== AnonymousMessenger-Py ===")
    while True:
        choice = input("\n1. Register\n2. Login\n3. Exit\nChoose: ")
        if choice == '1':
            user = register()
            if user:
                dashboard(user)
        elif choice == '2':
            user = login()
            if user:
                dashboard(user)
        elif choice == '3':
            break
        else:
            print("❌ Invalid option.")

def dashboard(user):
    while True:
        print(f"\n👤 Welcome, {user}")
        print("1. Send Anonymous Message")
        print("2. View Inbox")
        print("3. View All Users")
        print("4. Logout")
        choice = input("Choose: ")
        if choice == '1':
            send_message(user)
        elif choice == '2':
            view_inbox(user)
        elif choice == '3':
            list_users(user)
        elif choice == '4':
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
