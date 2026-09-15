import re


GAP_KEYWORDS = [
    "limitation",
    "limitations",
    "future work",
    "future research",
    "further research",
    "challenge",
    "challenges",
    "lack of",
    "remains unclear",
    "not well understood",
    "requires further",
    "needs further",
    "open problem",
    "unexplored",
    "underexplored",
    "scarce",
    "insufficient",
]


def find_gap_sentences(text):
    """
    Identify sentences that may indicate research gaps,
    limitations, challenges, or future research directions.
    """

    if not text:
        return []

    sentences = re.split(r'(?<=[.!?])\s+', text)

    gaps = []

    for sentence in sentences:

        sentence_lower = sentence.lower()

        for keyword in GAP_KEYWORDS:

            if keyword in sentence_lower:
                gaps.append(sentence.strip())
                break

    return gaps


def analyze_gaps(papers):
    """
    Analyze all retrieved papers and attach possible
    research gaps to each paper.
    """

    for paper in papers:

        gaps = find_gap_sentences(
            paper.get("abstract", "")
        )

        paper["gaps"] = gaps[:3]

    return papers