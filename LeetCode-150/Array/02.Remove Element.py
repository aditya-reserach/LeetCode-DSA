"""
Problem: Remove Element
-----------------------

You are given an integer array `nums` and an integer `val`. 
You need to remove all occurrences of `val` in `nums` **in-place**. 
The order of the elements may be changed. After removal, return the number 
of elements in `nums` that are not equal to `val`.

The function should:
1. Modify the array `nums` so that the first `k` elements contain the values 
   that are not equal to `val`.
2. Return `k` (the count of values not equal to `val`).
3. The values beyond index `k-1` in `nums` do not matter.

-------------------------------------------------------------------------------

Input Format:
- An integer array `nums` (0 <= len(nums) <= 100, 0 <= nums[i] <= 50).
- An integer `val` (0 <= val <= 100).

Output Format:
- An integer `k` representing the count of elements in `nums` not equal to `val`.
- The first `k` elements of `nums` should be the valid result (order does not matter).

-------------------------------------------------------------------------------

Example 1:
----------
Input: nums = [3, 2, 2, 3], val = 3
Output: 2, nums = [2, 2, _, _]

Explanation: 
Your function should return k = 2, with the first two elements of nums being 2.
The underscores (_) represent ignored values.

Example 2:
----------
Input: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
Output: 5, nums = [0, 1, 4, 0, 3, _, _, _]

Explanation: 
Your function should return k = 5, with the first five elements of nums 
containing 0, 1, 4, 0, 3 in any order.

-------------------------------------------------------------------------------

Constraints:
------------
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

-------------------------------------------------------------------------------
"""

# ======================================================================
# First Solution: Using Python's built-in functions (HackerRank style)
# ======================================================================

def removeElement_builtin(nums, val):
    """
    Remove all occurrences of `val` from nums using Python built-in features.
    """

    # Step 1: Use a list comprehension to create a new list with only elements not equal to val
    #         This scans the entire list once and collects valid elements.
    filtered = [x for x in nums if x != val]  # <-- built-in filter-like operation

    # Step 2: Calculate the count of valid elements (this is just the length of filtered)
    k = len(filtered)

    # Step 3: Copy the filtered elements back into nums (modify in-place)
    #         We replace nums[0:k] with the filtered values.
    nums[:k] = filtered

    # Step 4: Return the count (k) to the caller
    return k


# ---------------- Complexity Analysis ----------------
# Time Complexity:
# - List comprehension `[x for x in nums if x != val]` takes O(n) time, where n = len(nums).
# - Copying filtered values back into nums[:k] also takes O(k) time, with k <= n.
# - Total time complexity: O(n).
#
# Space Complexity:
# - The list comprehension creates a new list `filtered`, which can hold up to n elements.
# - Therefore, extra space is O(n).
# -----------------------------------------------------


# ======================================================================
# Second Solution: Manual implementation (without built-in shortcuts)
# ======================================================================

def removeElement_manual(nums, val):
    """
    Remove all occurrences of `val` from nums manually using two pointers.
    """

    # Step 1: Initialize a variable `index` to 0
    #         This will represent the "write pointer", i.e., the position
    #         where the next valid element (not equal to val) will be placed.
    index = 0

    # Step 2: Iterate over all indices of nums using a for loop
    for i in range(len(nums)):  # `i` is the "read pointer"
        # Step 3: Check if the current element nums[i] is NOT equal to val
        if nums[i] != val:
            # Step 4: Place the valid element nums[i] at the position nums[index]
            nums[index] = nums[i]
            # Step 5: Increment index to prepare for the next valid element
            index += 1

    # Step 6: Return the final value of index, which is the count of valid elements
    return index


# ---------------- Complexity Analysis ----------------
# Time Complexity:
# - The for loop iterates once over all n elements → O(n).
# - Each step inside the loop does constant work (comparison, assignment, increment).
# - Total time complexity: O(n).
#
# Space Complexity:
# - No additional lists or data structures are created.
# - Only a few integer variables (`index`, `i`) are used.
# - Total space complexity: O(1).
# -----------------------------------------------------


# ======================================================================
# Example Usage (Uncomment to test locally)
# ======================================================================
if __name__ == "__main__":
    # Example 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    print("Built-in Solution:", removeElement_builtin(nums1, val1), nums1)

    nums2 = [3, 2, 2, 3]
    val2 = 3
    print("Manual Solution:", removeElement_manual(nums2, val2), nums2)

    # Example 2
    nums3 = [0, 1, 2, 2, 3, 0, 4, 2]
    val3 = 2
    print("Built-in Solution:", removeElement_builtin(nums3, val3), nums3)

    nums4 = [0, 1, 2, 2, 3, 0, 4, 2]
    val4 = 2
    print("Manual Solution:", removeElement_manual(nums4, val4), nums4)


"""
Suggested Git Commit Message:
"Add Remove Element problem solutions with built-in and manual methods, including full problem statement, explanations, and complexity analysis"
"""
