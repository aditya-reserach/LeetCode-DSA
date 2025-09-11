"""
Problem Statement:
------------------
Given two sorted arrays `nums1` and `nums2` of sizes m and n respectively, return 
the median of the two sorted arrays.

You must achieve an overall run time complexity of O(log (m+n)).

Input Format:
-------------
- Two lists of integers:
  - nums1: first sorted array
  - nums2: second sorted array

Output Format:
--------------
- A float number representing the median of the combined sorted arrays.

Constraints:
------------
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6

Example 1:
----------
Input: nums1 = [1,3], nums2 = [2]
Output: 2.0
Explanation: merged array = [1,2,3], median is 2.

Example 2:
----------
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.5
Explanation: merged array = [1,2,3,4], median is (2+3)/2 = 2.5
--------------------------------------------------------------------------------
Solution 1: Using Python built-in functions/libraries
Solution 2: Manual implementation without using prebuilt helpers
--------------------------------------------------------------------------------
"""

from typing import List

# --------------------------------------------------------------------------------
# Solution 1: Using Python built-in functions (concatenate + sort + len)
# --------------------------------------------------------------------------------
class SolutionBuiltIn:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Step 1: Merge the two arrays into a single list using '+' operator
        merged = nums1 + nums2  

        # Step 2: Sort the merged array in ascending order
        merged.sort()  

        # Step 3: Calculate the number of elements in the merged array
        n = len(merged)  

        # Step 4: Check if the number of elements is even or odd
        if n % 2 == 0:
            # If even, median = average of two middle elements
            mid1 = n // 2 - 1  # First middle index
            mid2 = n // 2      # Second middle index
            median = (merged[mid1] + merged[mid2]) / 2.0
        else:
            # If odd, median = middle element
            median = merged[n // 2]

        # Step 5: Return the calculated median
        return median

"""
Time Complexity (Solution 1):
- Merging two arrays: O(m+n)
- Sorting the merged array: O((m+n) log(m+n))
- Median calculation: O(1)
- Overall: O((m+n) log(m+n))

Space Complexity (Solution 1):
- Storing merged array: O(m+n)
- Additional variables: O(1)
- Overall: O(m+n)
"""

# --------------------------------------------------------------------------------
# Solution 2: Manual implementation without using prebuilt functions like sort or len
# --------------------------------------------------------------------------------
class SolutionManual:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Finds median by manually merging two sorted arrays and calculating median
        without using built-in functions like sort() or len().
        """

        # Step 1: Manually calculate lengths of nums1 and nums2
        len1 = 0
        for _ in nums1:
            len1 += 1
        len2 = 0
        for _ in nums2:
            len2 += 1

        # Step 2: Total length of merged array
        total_len = len1 + len2

        # Step 3: Determine if total length is even
        is_even = (total_len % 2 == 0)

        # Step 4: Calculate middle index/indices
        mid_index1 = total_len // 2 - 1  # First middle element index (even case)
        mid_index2 = total_len // 2      # Second middle element or middle for odd

        # Step 5: Merge arrays manually using two pointers
        merged = []  # list to store merged elements
        i = 0        # pointer for nums1
        j = 0        # pointer for nums2
        count = 0    # count of elements merged

        while i < len1 or j < len2:
            # Take next element from nums1 if:
            #  - nums1 is not exhausted AND
            #  - (nums2 is exhausted OR current nums1 element <= current nums2 element)
            if i < len1 and (j >= len2 or nums1[i] <= nums2[j]):
                merged.append(nums1[i])
                i += 1
            else:
                # Otherwise take element from nums2
                merged.append(nums2[j])
                j += 1

            count += 1

            # Stop early if we have reached middle index
            if count > mid_index2:
                break

        # Step 6: Calculate median
        if is_even:
            median = (merged[mid_index1] + merged[mid_index2]) / 2.0
        else:
            median = merged[mid_index2]

        # Step 7: Return median
        return median

"""
Time Complexity (Solution 2):
- Manual length calculation: O(m+n)
- Manual merge up to median index: O((m+n)/2) ~ O(m+n)
- Median calculation: O(1)
- Overall: O(m+n)

Space Complexity (Solution 2):
- Storing merged elements up to median: O((m+n)/2) ~ O(m+n)
- Additional variables: O(1)
- Overall: O(m+n)
"""

# --------------------------------------------------------------------------------
# Example Usage
# --------------------------------------------------------------------------------
if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]

    # Using built-in solution
    solution1 = SolutionBuiltIn()
    print("Median using built-in functions:", solution1.findMedianSortedArrays(nums1, nums2))

    # Using manual solution
    solution2 = SolutionManual()
    print("Median using manual implementation:", solution2.findMedianSortedArrays(nums1, nums2))


