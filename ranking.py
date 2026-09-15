from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Pre-trained model for semantic similarity
model = SentenceTransformer("all-MiniLM-L6-v2")


def rank_papers(topic, papers):
    """
    Rank research papers according to semantic similarity
    with the user's research topic.
    """

    if not papers:
        return []

    # Create text representations of papers
    paper_texts = []

    for paper in papers:
        text = paper["title"]

        if paper.get("abstract"):
            text += ". " + paper["abstract"]

        paper_texts.append(text)

    # Convert topic and papers into embeddings
    topic_embedding = model.encode([topic])
    paper_embeddings = model.encode(paper_texts)

    # Calculate similarity
    similarities = cosine_similarity(
        topic_embedding,
        paper_embeddings
    )[0]

    # Add relevance score to each paper
    for paper, score in zip(papers, similarities):
        paper["relevance_score"] = round(float(score) * 100, 2)

    # Sort highest relevance first
    ranked_papers = sorted(
        papers,
        key=lambda x: x["relevance_score"],
        reverse=True
    )

    return ranked_papers


if __name__ == "__main__":
    print("Ranking module ready.")