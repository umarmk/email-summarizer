from gmail_auth import get_gmail_service
from email_reader import list_unread_messages, get_message_snippet

def main():
    msgs = list_unread_messages(max_results=3)
    if not msgs:
        print("No unread messages found.")
        return
    
    print(f"Found {len(msgs)} unread messages. Showing snippets:\n")
    for i, m in enumerate(msgs, 1):
        snippet = get_message_snippet(m["id"])
        print(f"{i}. {snippet}\n---\n")

if __name__ == "__main__":
    main()

