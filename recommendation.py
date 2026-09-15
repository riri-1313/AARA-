def recommend_papers(papers, top_n=5):
    """
    Recommend the most relevant research papers
    based on their semantic relevance scores.
    """

    if not papers:
        return []

    recommended = sorted(
        papers,
        key=lambda paper: paper.get("relevance_score", 0),
        reverse=True
    )

    return recommended[:top_n]


def display_recommendations(papers):
    """
    Display recommended research papers.
    """

    print("\n" + "=" * 60)
    print("RECOMMENDED RESEARCH PAPERS")
    print("=" * 60)

    for i, paper in enumerate(papers, 1):

        print(f"\n{i}. {paper['title']}")
        print(f"   Relevance Score: {paper['relevance_score']}%")
        print(f"   Year: {paper['year']}")
        print(f"   Citations: {paper['citations']}")
        print(f"   URL: {paper['url']}")