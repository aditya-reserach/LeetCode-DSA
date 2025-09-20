from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize a variable to keep track of the farthest index we can currently reach
        max_reach = 0
        
        # Get the total number of elements in the array
        n = len(nums)
        
        # Loop over each index from 0 to n-1
        for i in range(n):
            # If at any point the current index i is greater than max_reach,
            # it means we cannot even reach index i, so we must return False immediately
            if i > max_reach:
                return False
            
            # Calculate how far we can reach if we jump from this index
            possible_reach = i + nums[i]
            
            # Now update max_reach manually (without using built-in max)
            # If the new possible_reach is farther than current max_reach, update it
            if possible_reach > max_reach:
                max_reach = possible_reach
        
        # If we finish the loop without failing, it means we can reach the last index
        return True


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.canJump([2,3,1,1,4]))  # Expected True
    print(solution.canJump([3,2,1,0,4]))  # Expected False

