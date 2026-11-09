# 🧩 DSA Patterns Hub

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LeetCode](https://img.shields.io/badge/LeetCode-350%2B%20Solved-orange?logo=leetcode)](https://leetcode.com/MrYodha)
[![Profile](https://img.shields.io/badge/Author-Vaibhav%20Bajpai-blue)](https://github.com/VaibhavBajpaij)

A curated, interview-grade collection of **Data Structures & Algorithms** solutions categorized by underlying algorithmic patterns.

---

## 🎯 Philosophy: Pattern-Based Mastery

Rather than memorizing disjointed solutions to hundreds of problems, this repository categorizes problems by **core algorithmic patterns**. Recognizing the underlying pattern allows you to solve variations and unseen interview problems efficiently.

Each solution provides:
- 💡 **Intuition & Approach**: Why this pattern applies
- ⏱️ **Time Complexity**: Formal Big-O analysis
- 💾 **Space Complexity**: Auxiliary memory breakdown
- 🧪 **Test Cases**: Executable assertions and edge-case handling

---

## 🗺️ Algorithmic Pattern Roadmap

| # | Pattern | Key Concept | Optimal Complexity | Featured Problems |
|---|---|---|---|---|
| 01 | **Two Pointers** | Converging or parallel pointers on sorted/structured data | $O(N)$ Time, $O(1)$ Space | Two Sum II, 3Sum, Container With Most Water |
| 02 | **Sliding Window** | Expand & shrink window to track sub-arrays/sub-strings | $O(N)$ Time, $O(K)$ Space | Max Subarray of Size K, Longest Substring |
| 03 | **Fast & Slow Pointers** | Pointers advancing at different speeds (Floyd's Cycle) | $O(N)$ Time, $O(1)$ Space | Linked List Cycle, Middle of List, Happy Number |
| 04 | **Binary Search Variants** | Halving search space on monotonic conditions | $O(\log N)$ Time, $O(1)$ Space | Rotated Sorted Array, Search 2D Matrix |
| 05 | **Tree Traversals (DFS/BFS)** | Recursive depth exploration & level-by-level queue | $O(V + E)$ Time | Invert Tree, Level Order, Max Depth |

---

## 📂 Repository Structure

```text
dsa-patterns-hub/
├── 01-two-pointers/
│   ├── two_sum_sorted.py
│   ├── three_sum.py
│   └── container_with_most_water.py
├── 02-sliding-window/
│   ├── max_sum_subarray_k.py
│   └── longest_substring_no_repeats.py
├── 03-fast-slow-pointers/
│   └── linked_list_cycle.py
└── README.md
```

---

## 💻 Running the Code

All solutions are written in clean, type-annotated Python 3 and include self-contained unit tests.

```bash
# Run any solution directly:
python 01-two-pointers/two_sum_sorted.py
python 02-sliding-window/longest_substring_no_repeats.py
```

---

## 👤 Author

**Vaibhav Bajpai**
- **GitHub:** [@VaibhavBajpaij](https://github.com/VaibhavBajpaij)
- **LeetCode:** [MrYodha](https://leetcode.com/MrYodha)
- **Portfolio:** [vaibhav-b.vercel.app](https://vaibhav-b.vercel.app)
- **LinkedIn:** [vaibhav-bajpai-baj](https://linkedin.com/in/vaibhav-bajpai-baj)
