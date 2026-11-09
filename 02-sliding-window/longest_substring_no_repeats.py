"""
Pattern: Sliding Window (Dynamic Size with Hash Map)
Problem: Longest Substring Without Repeating Characters (LeetCode #3)
Difficulty: Medium

Description:
Given a string s, find the length of the longest substring without repeating characters.

Complexity:
- Time Complexity: O(N) where N is the length of string s. Each character is visited at most twice.
- Space Complexity: O(min(N, M)) where M is the size of the character set (charset dictionary).
"""

from typing import Dict


def length_of_longest_substring(s: str) -> int:
    """
    Finds length of longest substring without duplicate characters.
    
    Approach:
    Maintain a sliding window [left, right] and a map storing the last seen index
    of each character. When character at `right` is encountered again inside the
    current window, jump `left` to index + 1 of the previous occurrence.
    """
    last_seen: Dict[str, int] = {}
    max_len: int = 0
    left: int = 0

    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right
        current_window_len: int = right - left + 1
        if current_window_len > max_len:
            max_len = current_window_len

    return max_len


# --- Verification / Tests ---
if __name__ == "__main__":
    test_cases = [
        {"input": "abcabcbb", "expected": 3},
        {"input": "bbbbb", "expected": 1},
        {"input": "pwwkew", "expected": 3},
        {"input": "", "expected": 0},
        {"input": "dvdf", "expected": 3},
    ]

    for idx, tc in enumerate(test_cases, 1):
        result = length_of_longest_substring(tc["input"])
        assert result == tc["expected"], f"Failed test {idx}: got {result}, expected {tc['expected']}"
        print(f"[PASS] Test {idx}: input='{tc['input']}' -> len={result}")

    print("\nAll Longest Substring tests passed successfully!")
