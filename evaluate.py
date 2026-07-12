# evaluate.py
from dataset import STUDENT_QUERIES_DATASET
from grammar_rules import parse_query


def run_evaluation():
    print("Running evaluation")

    parsed_count = 0
    total_queries = len(STUDENT_QUERIES_DATASET)

    for idx, query in enumerate(STUDENT_QUERIES_DATASET, start=1):
        intent = parse_query(query)
        if intent != "unknown":
            parsed_count += 1
            status = f"[Success] -> Mapped to: {intent}"
        else:
            status = "[Failed] -> Triggered Fallback"

        print(f"Query {idx:02d}: '{query}'\n  Result: {status}\n")

    coverage = (parsed_count / total_queries) * 100
    print(f"\n\n\nEvaluation Metrics: Parsed {
          parsed_count}/{total_queries} queries cleanly.")
    print(f"Grammar Model Accuracy Coverage Score: {coverage:.2f}%")


if __name__ == "__main__":
    run_evaluation()
