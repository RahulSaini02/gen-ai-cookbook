import time

"""
121. Best Time to Buy and Sell Stock
---
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
  1 <= prices.length <= 105
  0 <= prices[i] <= 104
"""

"""
Solution:

# Brute Force
1. The max_profit function finds the maximum profit from a single buy-sell stock transaction by checking all possible pairs of days (i < j) and computing prices[j] - prices[i]. It keeps track of the highest profit found and returns it. Time complexity is O(n²) due to the nested loops.

# Optimized
2. We track the lowest price seen so far while iterating through the list of prices. For each day, we calculate the potential profit by selling at the current price and buying at the lowest price so far. We update the maximum profit whenever this potential profit is higher.

- Time Complexity: O(n)
- Space Complexity: O(1)

This ensures a single pass through the prices list with constant space.
"""

# prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1]


def maximum_profit_brute_force(prices: list[int]) -> int:
    max_profit = 0
    for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
            max_profit = (
                max_profit
                if prices[j] - prices[i] <= max_profit
                else prices[j] - prices[i]
            )
    return max_profit


def maximum_profit_optimized(prices: list[int]) -> int:
    max_profit = 0
    min_price = prices[0]

    for i in range(1, len(prices)):
        min_price = prices[i] if prices[i] < min_price else min_price
        current_profit = prices[i] - min_price
        max_profit = max(current_profit, max_profit)

    return max_profit


def run_test_cases(test_cases: list):
    start_time = time.time()  # Start timer
    for i in range(0, len(test_cases)):
        test = test_cases[i]
        prices = test["prices"]
        result = test["result"]
        case_start = time.time()
        output = maximum_profit_optimized(prices)
        case_end = time.time()

        if output == result:
            print(
                f"✅ Passed ({i + 1} / {len(test_cases)}): prices: {prices}, output: {output}, Time for execution {i + 1}: {case_end - case_start:.6f}"
            )
        else:
            print(
                f"❌ Failed ({i + 1} / {len(test_cases)}): prices: {prices}, expected output: {result}, output: {output}, Time for execution {i + 1}: {case_end - case_start:.6f}"
            )
    end_time = time.time()
    print(f"\n⏱ Total execution time: {end_time - start_time:.6f} seconds")


if __name__ == "__main__":
    test_cases = [
        {"prices": [7, 1, 5, 3, 6, 4], "result": 5},
        {"prices": [7, 6, 4, 3, 1], "result": 0},
    ]

    run_test_cases(test_cases)
