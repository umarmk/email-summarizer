from gmail_auth import get_gmail_service
import base64
import email
from typing import Optional

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

def get_email_body(msg_id: str) -> Optional[str]:
    """
    Fetches the full text/plain body of the email with id `msg_id`.
    Returns the decoded body string, or None if not found.
    """
    service = get_gmail_service()

    # Request the raw payload
    msg = service.users().messages().get(
        userId="me", id=msg_id, format="raw"
    ).execute()

    raw = msg.get("raw")
    if not raw:
        return None
    
    # Decode from base64url to bytes
    decoded_bytes = base64.urlsafe_b64decode(raw)

    # Parse into a MIME message
    mime_msg = email.message_from_bytes(decoded_bytes)

    # If multipart, find the text/plain part
    if mime_msg.is_multipart():
        for part in mime_msg.walk():
            content_type = part.get_content_type()
            content_disposition = part.get("Content-Disposition", "")
            if content_type == "text/plain" and "attachment" not in content_disposition:
                charset = part.get_content_charset() or "utf-8"
                return part.get_payload(decode=True).decode(charset, errors="replace")
    # Otherwise, decode the root payload
    else:
        charset = mime_msg.get_content_charset() or "utf-8"
        return mime_msg.get_payload(decode=True).decode(charset, errors="replace")
    
    return None