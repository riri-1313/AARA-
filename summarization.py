def summarize_text(text, max_sentences=3):
    """
    Generate a simple extractive summary from an abstract.
    """

    if not text:
        return "No abstract available."

    # Split abstract into sentences
    sentences = [
        sentence.strip()
        for sentence in text.replace("!", ".").replace("?", ".").split(".")
        if sentence.strip()
    ]

    # Return first few meaningful sentences
    summary = sentences[:max_sentences]

    return ". ".join(summary) + "."


def summarize_papers(papers):
    """
    Add summaries to all retrieved papers.
    """

    for paper in papers:
        paper["summary"] = summarize_text(
            paper.get("abstract", "")
        )

    return papers