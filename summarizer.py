from transformers import pipeline, AutoTokenizer

# Instantiate summarizer pipeline and tokenizer
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    tokenizer="facebook/bart-large-cnn",
)

# Load tokenizer separately for input length checking
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

def summarize_text(text: str, max_length: int = 130, min_length: int = 30) -> str:
    """
    Generate a concise summary of `text` using a local BART model.
    Handles long inputs by truncating to model's maximum sequence length.
    """

    if not text or not text.strip():
        return "No content to summarize."

    # BART-large-cnn has a maximum input length of 1024 tokens
    MAX_INPUT_TOKENS = 1000  # Leave some buffer for special tokens

    # Tokenize and check length
    tokens = tokenizer.encode(text, add_special_tokens=False)

    if len(tokens) > MAX_INPUT_TOKENS:
        # Truncate tokens and decode back to text
        truncated_tokens = tokens[:MAX_INPUT_TOKENS]
        text = tokenizer.decode(truncated_tokens, skip_special_tokens=True)
        print(f" ***Input truncated to {MAX_INPUT_TOKENS} tokens due to model limitations.***")

    try:
        # The pipeline returns a list of dicts: [{'summary_text': "..."}]
        result = summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False,
        )

        # Extract the summary text from the result
        summary = result[0]["summary_text"]
        return summary.strip()

    except Exception as e:
        print(f"Error during summarization: {e}")
        return f"Error: Could not summarize this content. ({str(e)[:100]}...)"