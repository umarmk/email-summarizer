from gmail_auth import get_gmail_service

def list_unread_messages(max_results=5):

    """
    Returns a list of message metadata for up to `max_results` unread emails.
    Each item is a dict with 'id' and 'threadId'.
    """
    service = get_gmail_service()
    results = (
        service.users()
        .messages()
        .list(userId="me", labelIds=["INBOX", "UNREAD"], maxResults=max_results)
        .execute()
    )
    return results.get("messages", [])

def get_message_snippet(msg_id):
    
    """
    Fetches the full message for `msg_id` and returns its snippet (first few lines).
    """
    service = get_gmail_service()
    msg = (
        service.users()
        .messages()
        .get(userId="me", id=msg_id, format="full")
        .execute()
    )
    return msg.get("snippet", "")

