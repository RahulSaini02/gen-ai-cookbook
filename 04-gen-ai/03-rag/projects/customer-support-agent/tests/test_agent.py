"""Example: Test customer support agent with predefined queries."""

import os
import sys

# Calculate the absolute path to the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Append the project root so Python can locate the 'src' directory
if project_root not in sys.path:
    sys.path.append(project_root)

from src.agent import handle_query, init_conversation, reset_conversation
from src.evals import EvalCase, run_eval_suite, save_eval_results


def main():
    """Test agent with sample queries."""

    # Test case 1: Return policy question
    messages = reset_conversation()
    init_conversation("CUST003", messages)

    print("\n" + "=" * 60)
    print("TEST 1: Return Policy Question")
    print("=" * 60)
    query1 = "Hello! I need help with my recent order to be returned"
    response1 = handle_query(query1, messages)
    print(f"Customer: {query1}")
    print(f"Maya: {response1}")

    # Test case 2: Follow-up question (multi-turn)
    print("\n" + "=" * 60)
    print("TEST 2: Follow-up Question (Multi-turn)")
    print("=" * 60)
    query2 = "Is my recent order eligible for return?"
    response2 = handle_query(query2, messages)
    print(f"Customer: {query2}")
    print(f"Maya: {response2}")

    # Test case 3: Different customer
    messages = reset_conversation()
    init_conversation("CUST001", messages)

    print("\n" + "=" * 60)
    print("TEST 3: Order Tracking")
    print("=" * 60)
    query3 = "Where is my order?"
    response3 = handle_query(query3, messages)
    print(f"Customer: {query3}")
    print(f"Maya: {response3}")


def run_evaluations():
    """Run evaluation suite on agent."""

    eval_cases = [
        # Docs-only: all three numbers live in the same "Return Window" doc
        # section, so this doubles as a regression check on chunk_doc — if a
        # near-empty header chunk outranks the real section, this fails.
        EvalCase(
            customer_id="CUST001",
            query="What's your return policy?",
            expected_keywords=["30 days", "60 days", "90 days"],
            forbidden_keywords=["do not accept returns", "no returns"],
            description="Return policy - basic question (docs-only)",
        ),
        # DB + docs: CUST003's real order status is "shipped" with no
        # delivery_date yet, so the window hasn't started. Requires both the
        # customer context (status) and the correct policy chunk (window).
        EvalCase(
            customer_id="CUST003",
            query="Can I return my recent order?",
            expected_keywords=["shipped", "30 days"],
            forbidden_keywords=[
                "delivered",
                "return has been processed",
                "refund has been issued",
            ],
            description="Return eligibility - order-specific (DB + RAG)",
        ),
        # expected_keywords is AND-only (see EvalCase), so it can't reliably
        # assert a paraphrasable refusal without false-failing correct
        # answers. Kept minimal (just on-topic) and pushed the real
        # correctness check onto forbidden_keywords instead, which doesn't
        # have that limitation.
        EvalCase(
            customer_id="CUST002",
            query="Do you accept Bitcoin?",
            expected_keywords=["bitcoin"],
            forbidden_keywords=[
                "yes, bitcoin",
                "bitcoin is accepted",
                "we do accept bitcoin",
                "we accept bitcoin",
                "bitcoin payments are accepted",
                "bitcoin works",
            ],
            description="Out-of-policy question - must not hallucinate",
        ),
    ]

    results = run_eval_suite(eval_cases)
    save_eval_results(results, prompt_version="v1")


if __name__ == "__main__":
    print("Customer Support Agent - Test Suite\n")

    # Run basic tests
    # main()

    # Run evaluations
    print("\n\nRunning Evaluation Suite...")
    run_evaluations()
