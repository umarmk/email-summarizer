# Email Summarizer

A command-line tool that retrieves your unread Gmail messages and produces concise summaries using a local BART model.

## Features

- OAuth2 read-only access to Gmail
- Full text/plain extraction of email bodies
- Local summarization via Hugging Face’s `facebook/bart-large-cnn`
- Tokenization and truncation for long emails

## Prerequisites

- Python 3.8 or higher
- A Gmail account with OAuth2 credentials

## Setup

1. Clone the repository and enter its folder:
   ```bash
   git clone https://github.com/umarmk/email-summarizer.git
   cd email-summarizer
   ```
