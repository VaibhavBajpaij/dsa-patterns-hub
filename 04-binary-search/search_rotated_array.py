"""
Pattern: Modified Binary Search
Problem: Search in Rotated Sorted Array (LeetCode #33)
Difficulty: Medium

Description:
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index.
Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

Complexity:
- Time Complexity: O(log N) where N is the length of nums. Search space halves each iteration.
- Space Complexity: O(1) auxiliary space.
"""

from typing import List


def search_rotated_array(nums: List[int], target: int) -> int:
    """
    Performs modified binary search on a rotated sorted array.
    
    Approach:
    In any rotated sorted array, at least one half (left or right of mid) is always sorted.
    1. Identify which half is normally sorted.
    2. Check if target lies within the boundaries of that sorted half.
    3. If yes, search that half; otherwise, search the opposite half.
    """
    left: int = 0
    right: int = len(nums) - 1

    while left <= right:
        mid: int = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Check if the left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Otherwise, the right half must be sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# --- Verification / Tests ---
if __name__ == "__main__":
    test_cases = [
        {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 0, "expected": 4},
        {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 3, "expected": -1},
        {"nums": [1], "target": 0, "expected": -1},
        {"nums": [1, 3], "target": 3, "expected": 1},
        {"nums": [5, 1, 3], "target": 5, "expected": 0},
    ]

    for idx, tc in enumerate(test_cases, 1):
        res = search_rotated_array(tc["nums"], tc["target"])
        assert res == tc["expected"], f"Failed test {idx}: got {res}, expected {tc['expected']}"
        print(f"[PASS] Test {idx}: nums={tc['nums']}, target={tc['target']} -> index={res}")

    print("\nAll Search Rotated Sorted Array tests passed successfully!")
