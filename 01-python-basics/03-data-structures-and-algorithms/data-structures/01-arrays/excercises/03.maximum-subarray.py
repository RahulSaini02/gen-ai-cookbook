import time

"""
53. Maximum Subarray
---
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
  1 <= nums.length <= 105
  -104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


def maximum_subarray(nums: list[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]
    for i in nums[1:]:
        current_sum = max(i, current_sum + i)
        max_sum = max(max_sum, current_sum)
    return max_sum


def run_test_cases(test_cases: list):
    start_time = time.time()  # Start timer
    for i in range(0, len(test_cases)):
        test = test_cases[i]
        nums = test["nums"]
        result = test["result"]
        case_start = time.time()
        output = maximum_subarray(nums)
        case_end = time.time()

        if output == result:
            print(
                f"✅ Passed ({i + 1} / {len(test_cases)}): nums: {nums}, output: {output}, Time for execution {i + 1}: {case_end - case_start:.6f}"
            )
        else:
            print(
                f"❌ Failed ({i + 1} / {len(test_cases)}): nums: {nums}, expected output: {result}, output: {output}, Time for execution {i + 1}: {case_end - case_start:.6f}"
            )
    end_time = time.time()
    print(f"\n⏱ Total execution time: {end_time - start_time:.6f} seconds")


if __name__ == "__main__":
    test_cases = [
        {"nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4], "result": 6},
        {"nums": [1], "result": 1},
        {"nums": [5, 4, -1, 7, 8], "result": 23},
    ]

    run_test_cases(test_cases)
