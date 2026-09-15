from retrieval import search_papers
from ranking import rank_papers
from summarization import summarize_papers
from gap_analysis import analyze_gaps
from recommendation import recommend_papers, display_recommendations
def main():

    print("=" * 60)
    print("        AARA 2.0 - Research Assistant")
    print("=" * 60)

    topic = input("\nEnter your research topic: ")

    print("\n[1/3] Retrieving research papers...")

    papers = search_papers(topic)

    if not papers:
        print("\nNo papers found. Please try another topic.")
        return

    print(f"Retrieved {len(papers)} papers.")

    print("\n[2/3] Ranking papers by relevance...")

    ranked_papers = rank_papers(topic, papers)

    print("\n[3/3] Generating paper summaries...")

    ranked_papers = summarize_papers(ranked_papers)
    print("\nAnalyzing potential research gaps...")

    ranked_papers = analyze_gaps(ranked_papers)
    print("\n" + "=" * 60)
    print("TOP RESEARCH PAPERS")
    print("=" * 60)

    for i, paper in enumerate(ranked_papers, 1):

        print(f"\n{i}. {paper['title']}")
        print(f"   Relevance: {paper['relevance_score']}%")
        print(f"   Year: {paper['year']}")
        print(f"   Citations: {paper['citations']}")
        print(f"   URL: {paper['url']}")
        print(f"   Summary: {paper['summary']}")
        if paper["gaps"]:
            print("   Potential Research Gaps:")

            for gap in paper["gaps"]:
                print(f"      - {gap}")
        else:
            print("   Potential Research Gaps: Not identified from abstract.")
        if paper["authors"]:
            print(f"   Authors: {', '.join(paper['authors'][:3])}")
    recommended = recommend_papers(ranked_papers)
    display_recommendations(recommended)

if __name__ == "__main__":
    main()