"""
Pattern: Two Pointers (Greedy Inward Squeeze)
Problem: Container With Most Water (LeetCode #11)
Difficulty: Medium

Description:
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Complexity:
- Time Complexity: O(N) where N is the number of vertical lines.
- Space Complexity: O(1) auxiliary space.
"""

from typing import List


def max_area(height: List[int]) -> int:
    """
    Computes the maximum area of water a container can hold.
    
    Approach:
    The area is determined by: (right - left) * min(height[left], height[right]).
    To maximize area, start at the widest possible span (left=0, right=len-1).
    At each step, greedily advance the pointer with the smaller height,
    because moving the taller pointer can never yield a larger area with a smaller width.
    """
    left: int = 0
    right: int = len(height) - 1
    max_water: int = 0

    while left < right:
        width: int = right - left
        current_height: int = min(height[left], height[right])
        current_area: int = width * current_height

        if current_area > max_water:
            max_water = current_area

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# --- Verification / Tests ---
if __name__ == "__main__":
    test_cases = [
        {"height": [1, 8, 6, 2, 5, 4, 8, 3, 7], "expected": 49},
        {"height": [1, 1], "expected": 1},
        {"height": [4, 3, 2, 1, 4], "expected": 16},
    ]

    for idx, tc in enumerate(test_cases, 1):
        ans = max_area(tc["height"])
        assert ans == tc["expected"], f"Failed test {idx}: got {ans}, expected {tc['expected']}"
        print(f"[PASS] Test {idx}: height={tc['height']} -> max_area={ans}")

    print("\nAll Container With Most Water tests passed successfully!")
