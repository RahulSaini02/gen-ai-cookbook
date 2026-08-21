import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from src.agent import handle_query, init_conversation


@dataclass
class EvalCase:
    """A test case for evaluation."""

    customer_id: str
    query: str
    expected_keywords: list[str]  # Must contain these
    forbidden_keywords: list[str]  # Must NOT contain these
    description: str


@dataclass
class EvalResult:
    """Results from a single eval case."""

    case: EvalCase
    passed: bool
    response: str
    missing_keywords: list[str]
    found_forbidden: list[str]


def eval_contains_keywords(
    response: str, keywords: list[str]
) -> tuple[bool, list[str]]:
    """Check if response contains required keywords."""
    response_lower = response.lower()
    missing = [kw for kw in keywords if kw.lower() not in response_lower]
    return len(missing) == 0, missing


def eval_no_forbidden(response: str, forbidden: list[str]) -> tuple[bool, list[str]]:
    """Check response doesn't contain forbidden phrases."""
    response_lower = response.lower()
    found = [fw for fw in forbidden if fw.lower() in response_lower]
    return len(found) == 0, found


def run_eval(eval_case: EvalCase, messages: list) -> EvalResult:
    """Run a single evaluation case."""
    response = handle_query(eval_case.query, messages.copy())

    has_keywords, missing = eval_contains_keywords(
        response, eval_case.expected_keywords
    )
    no_forbidden, found_forbidden = eval_no_forbidden(
        response, eval_case.forbidden_keywords
    )

    passed = has_keywords and no_forbidden

    return EvalResult(
        case=eval_case,
        passed=passed,
        response=response,
        missing_keywords=missing,
        found_forbidden=found_forbidden,
    )


def run_eval_suite(cases: list[EvalCase]) -> dict:
    """Run all eval cases and report results."""
    results = []
    for case in cases:
        messages = []
        init_conversation(case.customer_id, messages)
        result = run_eval(case, messages)
        results.append(result)

    passed = sum(1 for r in results if r.passed)
    total = len(results)

    print(f"\n{'=' * 60}")
    print(f"EVAL RESULTS: {passed}/{total} passed ({100 * passed // total}%)")
    print(f"{'=' * 60}\n")

    for result in results:
        status = "✓ PASS" if result.passed else "✗ FAIL"
        print(f"{status} | {result.case.description}")

        if result.missing_keywords:
            print(f"  Missing: {result.missing_keywords}")
        if result.found_forbidden:
            print(f"  Forbidden found: {result.found_forbidden}")
        print()

    return {"passed": passed, "total": total, "results": results}


def save_eval_results(
    results: dict, prompt_version: str = "v1", output_dir: str = "evals/results"
):
    """Save eval results for this prompt version."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    filename = f"{output_dir}/results_{prompt_version}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    eval_data = {
        "prompt_version": prompt_version,
        "timestamp": datetime.now().isoformat(),
        "passed": results["passed"],
        "total": results["total"],
        "score": results["passed"] / results["total"] if results["total"] > 0 else 0,
        "results": [
            {
                "description": r.case.description,
                "passed": r.passed,
                "query": r.case.query,
                "customer_id": r.case.customer_id,
                "missing_keywords": r.missing_keywords,
                "found_forbidden": r.found_forbidden,
                "response": r.response,
            }
            for r in results["results"]
        ],
    }

    with open(filename, "w") as f:
        json.dump(eval_data, f, indent=2)

    print(f"\n✓ Eval results saved to {filename}")
