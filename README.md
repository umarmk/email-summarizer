# Email Summarizer Agent

A command-line tool that automatically retrieves your unread Gmail messages and generates concise summaries using a local AI model. The tool processes emails intelligently, handles long content gracefully, and marks emails as read after summarization.

## Features

- OAuth2 read-only Gmail API integration
- Full email body extraction (text/plain content)
- Local AI summarization using Hugging Face BART-large-CNN model
- Intelligent text truncation for long emails (1000+ tokens)
- Automatic email marking as read after processing
- Robust error handling and user feedback
- No external API costs - runs entirely offline after initial setup

## Prerequisites

- Python 3.8 or higher
- Gmail account with API access enabled
- Approximately 2GB free disk space for AI model downloads

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/umarmk/email-summarizer-agent.git
   cd email-summarizer-agent
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Gmail API Setup

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Gmail API:
   - Navigate to "APIs & Services" > "Library"
   - Search for "Gmail API" and enable it
4. Create OAuth2 credentials:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth 2.0 Client IDs"
   - Choose "Desktop application" as the application type
   - Download the credentials JSON file
5. Rename the downloaded file to `credentials.json` and place it in the project root

## Configuration

1. Copy the environment template:

   ```bash
   cp .env.example .env
   ```

2. Edit `.env` file with your settings:
   ```
   GOOGLE_CREDENTIALS=credentials.json
   TOKEN_FILE=token.pickle
   ```

## Usage

Run the email summarizer:

```bash
python main.py
```

### First Run

- The application will open your default web browser for Gmail authentication
- Grant the requested permissions (read-only access to Gmail)
- The authentication token will be saved for future runs

### Subsequent Runs

- The tool will automatically use the saved authentication token
- No browser interaction required unless the token expires

### Sample Output

```
Summarizing your 3 most recent unread emails...

1. Original Email Snippet:
Hi team, Just a reminder that our sprint review is tomorrow at 10 AM...

 Summary:
   Sprint review scheduled for tomorrow at 10 AM. Team members should update tickets and prepare feature demos.

---
Marked as read.
---
```

## Configuration Options

You can modify behavior by editing `main.py`:

- `MAX_EMAILS`: Number of emails to process (default: 3)
- Summarization parameters in `summarizer.py`:
  - `max_length`: Maximum summary length (default: 130 tokens)
  - `min_length`: Minimum summary length (default: 30 tokens)

## Project Structure

```
email-summarizer-agent/
├── main.py              # Entry point and main processing loop
├── gmail_auth.py        # OAuth2 authentication handling
├── email_reader.py      # Gmail API integration and email processing
├── summarizer.py        # AI text summarization using BART
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
├── credentials.json     # Google API credentials (you provide)
├── token.pickle         # OAuth token storage (auto-generated)
└── README.md           # This file
```

## How It Works

1. **Authentication**: Uses OAuth2 to securely access your Gmail account with read-only permissions
2. **Email Retrieval**: Fetches the 3 most recent unread emails from your inbox
3. **Content Extraction**: Parses email MIME structure to extract plain text content
4. **AI Processing**: Uses Facebook's BART-large-CNN model to generate concise summaries
5. **Smart Truncation**: Automatically handles long emails by truncating to model limits (1000 tokens)
6. **Status Management**: Marks processed emails as read to avoid reprocessing

## Troubleshooting

### Common Issues

**"No module named 'transformers'"**

- Ensure you've activated your virtual environment and installed requirements

**"ModuleNotFoundError: No module named 'langchain_community'"**

- Run: `pip install langchain_community`

**"IndexError: index out of range"**

- This was fixed in the current version with intelligent text truncation

**"Authentication failed"**

- Delete `token.pickle` and run again to re-authenticate
- Verify your `credentials.json` file is valid

**"No unread messages to summarize"**

- The tool only processes unread emails
- Check your Gmail inbox for unread messages

### Performance Notes

- First run downloads ~2GB of AI model files (one-time)
- Subsequent runs are faster as models are cached locally
- Processing time: ~5-10 seconds per email depending on length

## Security & Privacy

- Uses OAuth2 with read-only Gmail permissions
- No email content is sent to external servers
- All AI processing happens locally on your machine
- Authentication tokens are stored securely in `token.pickle`

## Dependencies

Key packages:

- `transformers`: Hugging Face AI models
- `torch`: PyTorch for model inference
- `google-api-python-client`: Gmail API integration
- `google-auth-oauthlib`: OAuth2 authentication

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request
