"""
Pattern: Fast & Slow Pointers (Floyd's Tortoise and Hare Cycle Finding)
Problem: Linked List Cycle (LeetCode #141)
Difficulty: Easy

Description:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

Complexity:
- Time Complexity: O(N) where N is total number of nodes in the linked list.
- Space Complexity: O(1) auxiliary space (no hash set used).
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detects if a linked list contains a cycle using Floyd's Tortoise and Hare algorithm.
    
    Approach:
    Advance `slow` by 1 step and `fast` by 2 steps.
    If there is a cycle, the faster pointer is guaranteed to lap and meet
    the slower pointer inside the loop. If `fast` or `fast.next` reaches None,
    the list is acyclic.
    """
    if not head or not head.next:
        return False

    slow: Optional[ListNode] = head
    fast: Optional[ListNode] = head

    while fast and fast.next:
        slow = slow.next  # type: ignore
        fast = fast.next.next

        if slow is fast:
            return True

    return False


# --- Verification / Tests ---
if __name__ == "__main__":
    # Test 1: Cycle exists [3, 2, 0, -4] where -4 points to 2
    n1, n2, n3, n4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    assert has_cycle(n1) is True
    print("[PASS] Test 1: Linked list with cycle correctly detected.")

    # Test 2: No cycle [1, 2]
    a1, a2 = ListNode(1), ListNode(2)
    a1.next = a2
    assert has_cycle(a1) is False
    print("[PASS] Test 2: Acyclic linked list correctly returns False.")

    # Test 3: Empty list
    assert has_cycle(None) is False
    print("[PASS] Test 3: Empty linked list correctly returns False.")

    print("\nAll Linked List Cycle tests passed successfully!")
