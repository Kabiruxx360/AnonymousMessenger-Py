import json
import os

MESSAGES_FILE = 'data/messages.json'
USERS_FILE = 'data/users.json'

def load_messages():
    if not os.path.exists(MESSAGES_FILE):
        return []
    with open(MESSAGES_FILE, 'r') as f:
        return json.load(f)

def save_messages(messages):
    with open(MESSAGES_FILE, 'w') as f:
        json.dump(messages, f, indent=4)

def list_users(current_user):
    with open(USERS_FILE, 'r') as f:
        users = json.load(f)
    print("\n--- Users ---")
    for user in users:
        if user['username'] != current_user:
            print(f"- {user['username']}")

def send_message(sender):
    list_users(sender)
    receiver = input("\nEnter the username to message: ").strip()
    message = input("Enter your message: ").strip()

    messages = load_messages()
    messages.append({
        'from': sender,
        'to': receiver,
        'message': message
    })
    save_messages(messages)
    print("✅ Message sent anonymously.")

def view_inbox(user):
    messages = load_messages()
    inbox = [m for m in messages if m['to'] == user]
    print(f"\n📥 Inbox for {user} ({len(inbox)} messages)")
    if not inbox:
        print("No messages.")
    for msg in inbox:
        print(f"From: Anonymous\nMessage: {msg['message']}")
