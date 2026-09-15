# AARA 

## Intelligent Research Discovery and Analysis System

AARA  is an intelligent research assistant designed to help users discover and analyze academic literature from a given research topic.

The system retrieves research papers, ranks them according to semantic relevance, generates summaries, identifies potential research gaps, and recommends relevant papers.

## Features

- Academic paper retrieval using OpenAlex
- Semantic relevance ranking using Sentence Transformers
- Automatic extractive summarization
- Potential research gap detection
- Research paper recommendations
- Paper metadata including authors, year, citations, and DOI links

## System Workflow

Research Topic
→ Paper Retrieval
→ Semantic Relevance Ranking
→ Summarization
→ Research Gap Analysis
→ Paper Recommendation

## Technologies Used

- Python
- OpenAlex API
- Sentence Transformers
- Scikit-learn
- NumPy
- Pandas
- Requests

## Project Structure

```text
AARA 
│
├── gap_analysis.py
├── main.py
├── ranking.py
├── recommendation.py
├── retrieval.py
├── summarization.py
├── requirements.txt
├── README.md
└── .gitignore
