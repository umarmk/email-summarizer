from transformers import pipeline

# Instantiate summarizer pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    tokenizer="facebook/bart-large-cnn",
)

def summarize_text(text: str, max_length: int = 130, min_length: int = 30) -> str:

    """
    Generate a concise summary of `text` using a local model.
    """
    
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