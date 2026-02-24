"""Tool to extract and curate LeetCode problem links for a given topic."""


def extract_problem_links(topic: str) -> dict:
    """Extract relevant LeetCode problem links for a given DSA topic.

    Provides a curated set of LeetCode problem URLs organized by difficulty,
    covering commonly-tested patterns for the specified topic.

    Args:
        topic: The DSA topic to find problems for (e.g., 'binary-search',
               'dynamic-programming', 'two-pointers').

    Returns:
        A dict with 'topic', 'problemset_url', and 'curated_problems' keys.
    """
    # Normalize topic for URL formatting
    slug = topic.lower().strip().replace(" ", "-").replace("_", "-")

    # Curated problem mappings for popular topics
    curated = {
        "binary-search": [
            {"name": "Binary Search", "url": "https://leetcode.com/problems/binary-search/", "difficulty": "Easy"},
            {"name": "Search in Rotated Sorted Array", "url": "https://leetcode.com/problems/search-in-rotated-sorted-array/", "difficulty": "Medium"},
            {"name": "Find Minimum in Rotated Sorted Array", "url": "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/", "difficulty": "Medium"},
            {"name": "Median of Two Sorted Arrays", "url": "https://leetcode.com/problems/median-of-two-sorted-arrays/", "difficulty": "Hard"},
        ],
        "two-pointers": [
            {"name": "Two Sum II", "url": "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/", "difficulty": "Medium"},
            {"name": "3Sum", "url": "https://leetcode.com/problems/3sum/", "difficulty": "Medium"},
            {"name": "Container With Most Water", "url": "https://leetcode.com/problems/container-with-most-water/", "difficulty": "Medium"},
            {"name": "Trapping Rain Water", "url": "https://leetcode.com/problems/trapping-rain-water/", "difficulty": "Hard"},
        ],
        "dynamic-programming": [
            {"name": "Climbing Stairs", "url": "https://leetcode.com/problems/climbing-stairs/", "difficulty": "Easy"},
            {"name": "House Robber", "url": "https://leetcode.com/problems/house-robber/", "difficulty": "Medium"},
            {"name": "Longest Increasing Subsequence", "url": "https://leetcode.com/problems/longest-increasing-subsequence/", "difficulty": "Medium"},
            {"name": "Edit Distance", "url": "https://leetcode.com/problems/edit-distance/", "difficulty": "Hard"},
        ],
        "trees": [
            {"name": "Maximum Depth of Binary Tree", "url": "https://leetcode.com/problems/maximum-depth-of-binary-tree/", "difficulty": "Easy"},
            {"name": "Validate Binary Search Tree", "url": "https://leetcode.com/problems/validate-binary-search-tree/", "difficulty": "Medium"},
            {"name": "Binary Tree Level Order Traversal", "url": "https://leetcode.com/problems/binary-tree-level-order-traversal/", "difficulty": "Medium"},
            {"name": "Serialize and Deserialize Binary Tree", "url": "https://leetcode.com/problems/serialize-and-deserialize-binary-tree/", "difficulty": "Hard"},
        ],
        "graphs": [
            {"name": "Number of Islands", "url": "https://leetcode.com/problems/number-of-islands/", "difficulty": "Medium"},
            {"name": "Clone Graph", "url": "https://leetcode.com/problems/clone-graph/", "difficulty": "Medium"},
            {"name": "Course Schedule", "url": "https://leetcode.com/problems/course-schedule/", "difficulty": "Medium"},
            {"name": "Word Ladder", "url": "https://leetcode.com/problems/word-ladder/", "difficulty": "Hard"},
        ],
        "linked-list": [
            {"name": "Reverse Linked List", "url": "https://leetcode.com/problems/reverse-linked-list/", "difficulty": "Easy"},
            {"name": "Merge Two Sorted Lists", "url": "https://leetcode.com/problems/merge-two-sorted-lists/", "difficulty": "Easy"},
            {"name": "Linked List Cycle", "url": "https://leetcode.com/problems/linked-list-cycle/", "difficulty": "Easy"},
            {"name": "Merge k Sorted Lists", "url": "https://leetcode.com/problems/merge-k-sorted-lists/", "difficulty": "Hard"},
        ],
        "sliding-window": [
            {"name": "Best Time to Buy and Sell Stock", "url": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/", "difficulty": "Easy"},
            {"name": "Longest Substring Without Repeating Characters", "url": "https://leetcode.com/problems/longest-substring-without-repeating-characters/", "difficulty": "Medium"},
            {"name": "Minimum Window Substring", "url": "https://leetcode.com/problems/minimum-window-substring/", "difficulty": "Hard"},
            {"name": "Sliding Window Maximum", "url": "https://leetcode.com/problems/sliding-window-maximum/", "difficulty": "Hard"},
        ],
        "stack": [
            {"name": "Valid Parentheses", "url": "https://leetcode.com/problems/valid-parentheses/", "difficulty": "Easy"},
            {"name": "Min Stack", "url": "https://leetcode.com/problems/min-stack/", "difficulty": "Medium"},
            {"name": "Daily Temperatures", "url": "https://leetcode.com/problems/daily-temperatures/", "difficulty": "Medium"},
            {"name": "Largest Rectangle in Histogram", "url": "https://leetcode.com/problems/largest-rectangle-in-histogram/", "difficulty": "Hard"},
        ],
        "heap": [
            {"name": "Kth Largest Element in a Stream", "url": "https://leetcode.com/problems/kth-largest-element-in-a-stream/", "difficulty": "Easy"},
            {"name": "Top K Frequent Elements", "url": "https://leetcode.com/problems/top-k-frequent-elements/", "difficulty": "Medium"},
            {"name": "Find Median from Data Stream", "url": "https://leetcode.com/problems/find-median-from-data-stream/", "difficulty": "Hard"},
            {"name": "Merge k Sorted Lists", "url": "https://leetcode.com/problems/merge-k-sorted-lists/", "difficulty": "Hard"},
        ],
        "backtracking": [
            {"name": "Subsets", "url": "https://leetcode.com/problems/subsets/", "difficulty": "Medium"},
            {"name": "Permutations", "url": "https://leetcode.com/problems/permutations/", "difficulty": "Medium"},
            {"name": "Combination Sum", "url": "https://leetcode.com/problems/combination-sum/", "difficulty": "Medium"},
            {"name": "N-Queens", "url": "https://leetcode.com/problems/n-queens/", "difficulty": "Hard"},
        ],
    }

    problems = curated.get(slug, [])

    return {
        "topic": topic,
        "problemset_url": f"https://leetcode.com/problemset/?topicSlugs={slug}",
        "curated_problems": problems,
        "note": f"Found {len(problems)} curated problems."
        if problems
        else f"No curated list for '{topic}'. Use the problemset URL to browse problems on LeetCode.",
    }