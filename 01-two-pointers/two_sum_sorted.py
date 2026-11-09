"""
Pattern: Two Pointers (Converging Pointers)
Problem: Two Sum II - Input Array Is Sorted (LeetCode #167)
Difficulty: Medium

Description:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.

Complexity:
- Time Complexity: O(N) where N is the length of numbers. Each element is visited at most once.
- Space Complexity: O(1) auxiliary space, using only two pointer variables.
"""

from typing import List, Optional


def two_sum_sorted(numbers: List[int], target: int) -> Optional[List[int]]:
    """
    Finds two 1-based indices in a sorted array that sum to target.
    
    Approach:
    Initialize two pointers: left at start (0), right at end (len-1).
    Since the array is sorted:
      - If sum < target: increment left to increase total.
      - If sum > target: decrement right to decrease total.
      - If sum == target: return 1-based indices [left + 1, right + 1].
    """
    left: int = 0
    right: int = len(numbers) - 1

    while left < right:
        current_sum: int = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None


# --- Verification / Tests ---
if __name__ == "__main__":
    test_cases = [
        {"numbers": [2, 7, 11, 15], "target": 9, "expected": [1, 2]},
        {"numbers": [2, 3, 4], "target": 6, "expected": [1, 3]},
        {"numbers": [-1, 0], "target": -1, "expected": [1, 2]},
    ]

    for i, test in enumerate(test_cases, 1):
        result = two_sum_sorted(test["numbers"], test["target"])
        assert result == test["expected"], f"Test {i} failed: got {result}, expected {test['expected']}"
        print(f"[PASS] Test case {i}: numbers={test['numbers']}, target={test['target']} -> {result}")

    print("\nAll Two Sum II tests passed successfully!")
