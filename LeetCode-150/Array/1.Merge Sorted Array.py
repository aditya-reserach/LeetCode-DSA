"""
Problem: 88. Merge Sorted Array (LeetCode / HackerRank Style)

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

---

Input / Output Formats:
- Input:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6], n = 3

- Output:
    [1,2,2,3,5,6]

---

Constraints:
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10^9 <= nums1[i], nums2[j] <= 10^9

---

Examples:

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]

---

Follow up: Can you come up with an algorithm that runs in O(m + n) time?

-------------------------------------------------------------------------------------
Solution 1: Using Python built-in functions (simple approach with sort())
Solution 2: Manual in-place merge with two pointers (optimal O(m+n), O(1) space)
-------------------------------------------------------------------------------------
"""

# -------------------------------------------------------------------------------------
# Solution 1: Using Python built-in functions/libraries
# -------------------------------------------------------------------------------------
class SolutionBuiltIn(object):
    def merge(self, nums1, m, nums2, n):
        # Loop through each element of nums2
        for j in range(n):  
            # Place nums2[j] into nums1 starting from index m
            # Explanation: nums1 already has extra space (0s) at the end, so we overwrite them
            nums1[m + j] = nums2[j]
        # Sort nums1 in-place using Python's built-in sort()
        nums1.sort()


"""
Time Complexity Analysis (Solution 1):
---------------------------------------
1. Copying elements from nums2 into nums1 takes O(n) time (loop runs n times).
2. Sorting nums1 of total size (m+n) takes O((m+n) * log(m+n)) time using Timsort.
Total = O(n) + O((m+n) log(m+n)) = O((m+n) log(m+n)).

Space Complexity Analysis (Solution 1):
----------------------------------------
- The in-place sort() in Python uses O(log(m+n)) space due to recursion stack (Timsort).
- No extra arrays created manually.
Total = O(log(m+n)) extra space.
"""


# -------------------------------------------------------------------------------------
# Solution 2: Manual optimal solution with two pointers (from the back)
# -------------------------------------------------------------------------------------
class SolutionOptimal(object):
    def merge(self, nums1, m, nums2, n):
        # Initialize pointer i at the last valid element in nums1
        i = m - 1
        # Initialize pointer j at the last element in nums2
        j = n - 1
        # Initialize pointer k at the last position of nums1
        k = m + n - 1

        # Loop while both i and j are valid
        while i >= 0 and j >= 0:
            # Compare nums1[i] and nums2[j]
            if nums1[i] > nums2[j]:
                # If nums1[i] is bigger, place it at nums1[k]
                nums1[k] = nums1[i]
                # Move pointer i one step back
                i -= 1
            else:
                # If nums2[j] is bigger or equal, place it at nums1[k]
                nums1[k] = nums2[j]
                # Move pointer j one step back
                j -= 1
            # Move pointer k one step back (since we filled one slot)
            k -= 1

        # If any elements remain in nums2, copy them into nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


"""
Time Complexity Analysis (Solution 2):
---------------------------------------
1. Each element from nums1 and nums2 is compared/placed exactly once.
2. Loop runs at most (m+n) times.
Total = O(m + n).

Space Complexity Analysis (Solution 2):
----------------------------------------
- All operations are done in-place inside nums1.
- Only a few integer variables (i, j, k) are used.
Total = O(1) extra space.
"""



