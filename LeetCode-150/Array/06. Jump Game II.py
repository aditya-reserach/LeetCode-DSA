"""
Problem: Jump Game II

You are given a 0-indexed array of integers nums of length n. 
You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. 
In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and i + j < n

Return the minimum number of jumps to reach index n - 1. 
The test cases are generated such that you can reach index n - 1.

-----------------------------------------------------------------------
Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

-----------------------------------------------------------------------
Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].

-----------------------------------------------------------------------
Input Format:
- A single list/array of integers (nums), where each integer represents the maximum jump length at that position.

Output Format:
- Return an integer representing the minimum number of jumps to reach the last index.
-----------------------------------------------------------------------
"""

# ============================================================
# Solution 1 (Using built-in max function - HackerRank style)
# ============================================================

def jump_builtins(nums):
    n = len(nums)           # 🔹 total number of elements
    jumps = 0               # 🔹 counts total jumps
    current_end = 0         # 🔹 farthest reachable index with current jumps
    farthest = 0            # 🔹 farthest reachable index from current layer

    # 🔹 loop through each index except the last one
    for i in range(n - 1):
        # 🔹 calculate farthest reach from current index
        farthest = max(farthest, i + nums[i])
        # Explanation: i + nums[i] = farthest we can jump from index i
        # max ensures we always store the maximum reach

        # 🔹 if we've reached the end of current jump layer
        if i == current_end:
            jumps += 1               # 🔹 take a jump
            current_end = farthest   # 🔹 update the end of current jump

    return jumps                      # 🔹 return total minimum jumps

# ============================================================
# Solution 2 (Manual implementation without built-ins)
# ============================================================

def jump_manual(nums):
    n = len(nums)           # 🔹 total number of elements
    jumps = 0               # 🔹 counts total jumps
    current_end = 0         # 🔹 farthest reachable index with current jumps
    farthest = 0            # 🔹 farthest reachable index from current layer

    # 🔹 loop through each index except the last one
    for i in range(n - 1):
        # 🔹 calculate farthest reach from current index manually
        possible_reach = i + nums[i]  # 🔹 farthest we can jump from index i
        if possible_reach > farthest: # 🔹 update farthest if possible_reach is farther
            farthest = possible_reach

        # 🔹 if we've reached the end of current jump layer
        if i == current_end:
            jumps += 1               # 🔹 take a jump
            current_end = farthest   # 🔹 update the end of current jump

    return jumps                      # 🔹 return total minimum jumps

# ============================================================
# Testing both solutions
# ============================================================

if __name__ == "__main__":
    # Example 1
    nums1 = [2, 3, 1, 1, 4]
    print("Built-in solution (Example 1):", jump_builtins(nums1))  # Expected: 2
    print("Manual solution (Example 1):", jump_manual(nums1))      # Expected: 2

    # Example 2
    nums2 = [2, 3, 0, 1, 4]
    print("Built-in solution (Example 2):", jump_builtins(nums2))  # Expected: 2
    print("Manual solution (Example 2):", jump_manual(nums2))      # Expected: 2

# ============================================================
# Time and Space Complexity Analysis
# ============================================================

"""
Solution 1 (Built-in max):
--------------------------
- Time Complexity:
  * Loop runs from index 0 to n-2 → O(n)
  * max(farthest, i + nums[i]) is O(1)
  * Total time complexity = O(n)
- Space Complexity:
  * Uses only a few integers: n, jumps, current_end, farthest
  * No extra arrays → O(1)

Solution 2 (Manual):
--------------------
- Time Complexity:
  * Loop runs from index 0 to n-2 → O(n)
  * Inside loop: constant-time operations → O(1)
  * Total time complexity = O(n)
- Space Complexity:
  * Only integers: n, jumps, current_end, farthest, possible_reach
  * O(1)

Both solutions are optimal in time and space.
"""
