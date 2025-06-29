from email_reader import list_unread_messages, get_email_body
from summarizer import summarize_text

def main():
    
    # How many emails to process
    MAX_EMAILS = 5

    # Fetch metadata for the top N unread emails
    msgs = list_unread_messages(max_results = MAX_EMAILS)
    if not msgs:
        print("No unread messages to summarize.")
        return
    
    print(f"Summarizing your {len(msgs)} most recent unread emails...\n")

    # For each message, fetch the body and summarize it
    for idx, m in enumerate(msgs, start=1):
        body = get_email_body(m["id"])
        if not body:
            print(f"{idx}. [Could not retrieve body]\n---\n")
            continue

        print(f"{idx}. Original Email Snippet:\n{body[:200]}...\n")  # show first 200 chars
        summary = summarize_text(body)
        print(f" Summary:\n   {summary}\n")
        print("---\n")

if __name__ == "__main__":
    main()

