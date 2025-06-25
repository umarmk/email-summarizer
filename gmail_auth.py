import os, pickle
from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Load environment variables from .env file
load_dotenv()

CREDS_PATH = os.getenv("GOOGLE_CREDENTIALS")
TOKEN_PATH = os.getenv("TOKEN_FILE")
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def get_gmail_service():

    # Returns an authorized Gmail API service instance.
    # - Checks for existing token in TOKEN_PATH.
    # - If missing/expired, runs OAuth flow in your browser.
    # - Stores refreshed token back to TOKEN_PATH.
    
    creds = None

    # Check if token exists and is valid
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, "rb") as token_file:
            creds = pickle.load(token_file)
    
    # If no valid credentials, launch OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open(TOKEN_PATH, "wb") as token_file:
            pickle.dump(creds, token_file)
    
    # Build the Gmail API service
    service = build("gmail", "v1", credentials=creds)
    return service

