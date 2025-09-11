"""
Problem Statement:
------------------
Given an array of integers `nums` and an integer `target`, return the indices of the 
two numbers such that they add up to the target.

You may assume that each input would have exactly one solution, and you may not use 
the same element twice. You can return the answer in any order.

Input Format:
-------------
- The first line contains an integer `n`, the size of the array.
- The second line contains `n` space-separated integers, representing the array `nums`.
- The third line contains the integer `target`.

Output Format:
--------------
- A list containing two integers, the indices of the two numbers that add up to `target`.

Constraints:
------------
- 2 <= n <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Exactly one valid answer exists.

Example:
--------
Input:
4
2 7 11 15
9

Output:
[0, 1]

Explanation:
------------
nums[0] + nums[1] = 2 + 7 = 9, so we return [0, 1].

--------------------------------------------------------------------------------
Solution 1: Hash Map (using Python built-in dict)
Solution 2: Manual nested loops without using built-in helpers (manual length, manual sum check)
--------------------------------------------------------------------------------
"""

# --------------------------------------------------------------------------------
# Solution 1: Hash Map Approach (efficient) using Python's built-in dictionary
# --------------------------------------------------------------------------------

class SolutionHashMap:
    def twoSum(self, nums, target):
        # Create an empty dictionary (hash map) to store numbers and their indices
        numhash = {}  

        # Loop over the range of indices of the list nums
        for i in range(len(nums)):
            # Calculate the complement needed to reach the target
            result = target - nums[i]  

            # Check if this complement already exists in the hash map
            if result in numhash:  
                # If found, return the stored index of complement and current index
                return [numhash[result], i]  

            # Otherwise, store the current number with its index in the hash map
            numhash[nums[i]] = i  

        # If no solution is found (though problem guarantees one), return empty list
        return []  

"""
Time Complexity (Solution 1):
-----------------------------
- The loop runs `n` times, where `n` is the length of nums.
- Dictionary lookup (`if result in numhash`) is O(1) on average due to hashing.
- Dictionary insertion (`numhash[nums[i]] = i`) is also O(1) on average.
- Total = O(n).

Space Complexity (Solution 1):
------------------------------
- We use an extra dictionary that stores at most `n` key-value pairs.
- Thus, space complexity = O(n).
"""

# --------------------------------------------------------------------------------
# Solution 2: Manual Brute Force Approach (without prebuilt helpers like len() or dict)
# --------------------------------------------------------------------------------

class SolutionManual:
    def twoSum(self, nums, target):
        # Step 1: find length manually (no len())
        n = 0                        # Initialize counter to 0
        for _ in nums:               # Iterate through nums just to count elements
            n += 1                   # Increment counter for each element

        # Step 2: nested loop to check all pairs
        i = 0                        # Start index for outer loop
        while i < n:                 # Outer loop iterates over first element
            j = i + 1                # Inner loop starts from the next element
            while j < n:             # Inner loop iterates over second element
                # Step 3: check sum manually by directly adding two numbers
                if nums[i] + nums[j] == target:  
                    # Step 4: return indices in a list
                    return [i, j]    
                j += 1               # Move to next index in inner loop
            i += 1                   # Move to next index in outer loop

        # Step 5: if no solution found, return empty list
        return []  

"""
Time Complexity (Solution 2):
-----------------------------
- Outer loop runs `n` times.
- Inner loop runs up to `n` times for each outer loop.
- Total number of iterations = O(n^2).
- Each sum check is O(1).
- Thus total = O(n^2).

Space Complexity (Solution 2):
------------------------------
- Only a few variables (`n`, `i`, `j`) are used in addition to input array.
- No extra significant storage, so O(1).
"""

# --------------------------------------------------------------------------------
# Example usage for testing
# --------------------------------------------------------------------------------
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    
    print("Solution 1 (Hash Map):", SolutionHashMap().twoSum(nums, target))
    print("Solution 2 (Manual):", SolutionManual().twoSum(nums, target))


"""
Suggested Git Commit Message:
-----------------------------
"Add Two Sum solutions: hash map (O(n)) and manual brute force (O(n^2)) with detailed explanations"
"""
