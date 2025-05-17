import time

"""
1. Two Sum
---
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:
  2 <= nums.length <= 104
  -109 <= nums[i] <= 109
  -109 <= target <= 109

Only one valid answer exists.
"""

"""
Soluiton:

1. Loop the array two times and check if the sum of elements match the target.
"""


def two_sum(a: list[int], target: int) -> list[int]:
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == target:
                return [i, j]
    return []


def run_test_cases(test_cases: list):
    start_time = time.time()  # Start timer
    for i in range(0, len(test_cases)):
        test = test_cases[i]
        nums = test["nums"]
        target = test["target"]
        result = test["result"]
        case_start = time.time()
        output = two_sum(nums, target)
        case_end = time.time()

        if output == result or output == result[::-1]:
            print(
                f"✅ Passed ({i + 1} / {len(test_cases)}): nums: {nums}, target: {target}, output: {output}, Time for execution {i + 1}: {case_end - case_start:.6f}"
            )
        else:
            print(
                f"❌ Failed ({i + 1} / {len(test_cases)}): nums: {nums}, target: {target}, expected output: {result}, output: {output}, Time for execution {i + 1}: {case_end - case_start:.6f}"
            )
    end_time = time.time()
    print(f"\n⏱ Total execution time: {end_time - start_time:.6f} seconds")


if __name__ == "__main__":
    test_cases = [
        {"nums": [2, 7, 11, 15], "target": 9, "result": [0, 1]},
        {"nums": [3, 2, 4], "target": 6, "result": [1, 2]},
        {"nums": [3, 3], "target": 6, "result": [0, 1]},
    ]

    run_test_cases(test_cases)
