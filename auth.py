import json
import os

USERS_FILE = 'data/users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def register():
    print("\n--- Register ---")
    username = input("Choose a username: ").strip()
    users = load_users()
    if any(u['username'] == username for u in users):
        print("❌ Username already exists.")
        return None

    password = input("Choose a password: ").strip()
    users.append({'username': username, 'password': password})
    save_users(users)
    print("✅ Registered successfully.")
    return username

def login():
    print("\n--- Login ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    users = load_users()
    for user in users:
        if user['username'] == username and user['password'] == password:
            print("✅ Logged in successfully.")
            return username
    print("❌ Invalid credentials.")
    return None
