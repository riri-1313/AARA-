import requests


OPENALEX_API = "https://api.openalex.org/works"


def search_papers(topic, limit=8):
    """
    Retrieve research papers from OpenAlex.
    """

    params = {
        "search": topic,
        "per-page": limit
    }

    try:
        response = requests.get(
            OPENALEX_API,
            params=params,
            timeout=20
        )

        response.raise_for_status()
        data = response.json()

        papers = []

        for work in data.get("results", []):

            title = work.get("title")

            if not title:
                continue

            authors = []

            for author in work.get("authorships", []):
                author_name = author.get("author", {}).get("display_name")

                if author_name:
                    authors.append(author_name)

            abstract = ""

            # OpenAlex stores abstracts as an inverted index.
            inverted_index = work.get("abstract_inverted_index")

            if inverted_index:
                words = []

                for word, positions in inverted_index.items():
                    for position in positions:
                        words.append((position, word))

                words.sort()
                abstract = " ".join(word for _, word in words)

            papers.append({
                "title": title,
                "abstract": abstract,
                "authors": authors,
                "year": work.get("publication_year"),
                "url": work.get("doi") or work.get("id"),
                "citations": work.get("cited_by_count", 0)
            })

        return papers

    except requests.RequestException as error:

        print(f"\nError retrieving papers: {error}")

        return []


if __name__ == "__main__":

    topic = input("Enter research topic: ")

    print("\nSearching research papers...")

    papers = search_papers(topic)

    if not papers:

        print("\nNo papers were retrieved.")

    else:

        print(f"\nFound {len(papers)} papers:\n")

        for i, paper in enumerate(papers, 1):

            print(f"{i}. {paper['title']}")
            print(f"   Year: {paper['year']}")
            print(f"   Citations: {paper['citations']}")
            print(f"   URL: {paper['url']}")
            print()