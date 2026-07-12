# evaluate_ambiguity.py
# Some errors pop up, warnings too but it is completely ok
# MISALIGNED should be handled tho



import nltk
from nltk import CFG
from dataset import STUDENT_QUERIES_DATASET
from grammar_rules import CFG_RULES, clean_and_tokenize, parse_query
from responses import get_simulated_response


def test_grammar_properties():
    """Analyzes the CFG string for left recursion and rule redundancies."""
    print("Executing Structural Grammar Analytics...")
    lines = [line.strip() for line in CFG_RULES.split('\n') if '->' in line]

    left_recursive_rules = []
    redundant_check = {}

    for line in lines:
        left_side, right_side = line.split('->')
        left_side = left_side.strip()
        productions = [p.strip() for p in right_side.split('|')]

        # Check for Direct Left Recursion
        for prod in productions:
            first_token = prod.split()[0].replace("'", "")
            if first_token == left_side:
                left_recursive_rules.append(f"{left_side} -> {prod}")

        # Accumulate for Redundancy checks
        for prod in productions:
            if prod in redundant_check:
                redundant_check[prod].append(left_side)
            else:
                redundant_check[prod] = [left_side]

    # Display Left Recursion Results
    if left_recursive_rules:
        print(f"[Warning] Left Recursion Found in {
              len(left_recursive_rules)} rules:")
        for r in left_recursive_rules:
            print(f"   -> {r}")
    else:
        print("Grammar is completely free of Left Recursion.")

    # Display Redundancy Results
    redundancies = {k: v for k, v in redundant_check.items() if len(
        v) > 1 and k not in ["'is'", "'when' 'is'"]}
    if redundancies:
        print(f"[Warning] {
              len(redundancies)} duplicate terminal mappings detected:")
        for prod, non_terms in redundancies.items():
            print(f"   Token {prod} is replicated across: {non_terms}")
    else:
        print("No unnecessary rule redundancies found.")


def run_comprehensive_evaluation():
    """Runs structural parse metrics and response relevance mapping across the dataset."""
    print("Running the ambiguity checks\n\n")

    grammar = CFG.fromstring(CFG_RULES)
    parser = nltk.ChartParser(grammar)

    total_queries = len(STUDENT_QUERIES_DATASET)
    parsed_cleanly = 0
    ambiguous_count = 0
    failed_count = 0

    def get_ground_truth_intent(index):
        if index <= 8:
            return "exam_timetable"
        if index <= 16:
            return "missing_marks"
        if index <= 24:
            return "attachment_logbook"
        if index <= 32:
            return "graduation_list"
        return "office_appointment"

    for idx, query in enumerate(STUDENT_QUERIES_DATASET, start=1):
        tokens = clean_and_tokenize(query)
        ground_truth = get_ground_truth_intent(idx)

        # Pull tree structural variances
        trees = list(parser.parse(tokens))
        num_trees = len(trees)

        predicted_intent = parse_query(query)
        response = get_simulated_response(predicted_intent)

        # Test for Ambiguity
        if num_trees > 1:
            ambiguous_count += 1
            status = f"[Warning] AMBIGUOUS ({num_trees} parse trees generated)"
        elif num_trees == 1:
            parsed_cleanly += 1
            status = "CLEANLY PARSED"
        else:
            failed_count += 1
            status = "[Error] STRUCTURAL MISS (Used Keyword Fallback)"

        # Evaluate AI Response Relevance
        relevance = "EXCELLENT Match" if predicted_intent == ground_truth else "MISALIGNED Content"

        print(f"Query {idx:02d}: '{query}'")
        print(f"  Parsing Status: {status}")
        print(f"  Intent Mapping: Expected: [{ground_truth}] | Got: [{
              predicted_intent}] ({relevance})")
        print(f"  Response Preview: {response[:60]}...\n")

    # Print Final Summarized Quantitative Metrics
    coverage_score = (parsed_cleanly / total_queries) * 100
    accuracy_score = (sum(1 for idx, q in enumerate(STUDENT_QUERIES_DATASET, 1) if parse_query(
        q) == get_ground_truth_intent(idx)) / total_queries) * 100

    print("Final report")
    print(f"• Total Dataset Sample Verified : {
          total_queries} Queries[cite: 1]")
    print(f"• Pure CFG Structural Coverage  : {
          coverage_score:.2f}% ({parsed_cleanly}/{total_queries})")
    print(f"• Ambiguity Rate               : {
          ((ambiguous_count/total_queries)*100):.2f}%")
    print(f"• Fallback Engine Dependency    : {
          ((failed_count/total_queries)*100):.2f}%")
    print(f"• Intent / Response Accuracy    : {accuracy_score:.2f}%")


if __name__ == "__main__":
    test_grammar_properties()
    run_comprehensive_evaluation()
