from email_reader import list_unread_messages, get_email_body

def main():
    msgs = list_unread_messages(max_results=1)
    if not msgs:
        print("No unread messages.")
        return

    body = get_email_body(msgs[0]["id"])
    print("Full email body:\n")
    print(body)

if __name__ == "__main__":
    main()

