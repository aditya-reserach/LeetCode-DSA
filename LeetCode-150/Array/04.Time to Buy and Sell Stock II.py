"""
Problem: Best Time to Buy and Sell Stock II
Difficulty: Medium
Topics: Array, Greedy
Companies: Premium Lock Icon (Common in many coding platforms)

Problem Statement:
You are given an integer array `prices` where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: 
Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock.

Constraints:
1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4
"""

from typing import List

# ================================================================
# Solution 1: Using built-in Python functionality (your original code)
# ================================================================

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)                 # Store the number of days
        profit = 0                      # Initialize total profit to 0

        # Loop through each day starting from day 1
        for i in range(1, n):
            if prices[i] > prices[i - 1]:   # If today's price is higher than yesterday
                profit += prices[i] - prices[i - 1]  # Add the difference to total profit
        return profit                      # Return the maximum profit

"""
Time Complexity Analysis for Solution 1:
- We loop through the array exactly once → O(n)
- Each operation inside the loop is O(1)
- Total Time Complexity: O(n)
- Space Complexity: We only use constant extra space → O(1)
"""

# ================================================================
# Solution 2: Manual calculation without built-in helpers
# ================================================================

class SolutionManual:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)            # Store the number of days
        total_profit = 0           # Initialize total profit to 0
        i = 0                      # Start from the first day

        while i < n - 1:           # Loop until the second last day
            # Find the next local minimum to buy
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            buy_price = prices[i]  # Buy at the local minimum

            # Find the next local maximum to sell
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            sell_price = prices[i] # Sell at the local maximum

            total_profit += sell_price - buy_price  # Add profit for this transaction

        return total_profit         # Return total profit

"""
Time Complexity Analysis for Solution 2:
- Each element is visited at most twice (once while finding min, once while finding max) → O(n)
- Space Complexity: We only use constant extra variables → O(1)
- Total Time Complexity: O(n), Space Complexity: O(1)
"""

# ================================================================
# Test Cases to verify correctness
# ================================================================

if __name__ == "__main__":
    prices1 = [7,1,5,3,6,4]
    prices2 = [1,2,3,4,5]
    prices3 = [7,6,4,3,1]

    sol1 = Solution()
    sol2 = SolutionManual()

    print("Solution 1 Results:")
    print(sol1.maxProfit(prices1))  # Output: 7
    print(sol1.maxProfit(prices2))  # Output: 4
    print(sol1.maxProfit(prices3))  # Output: 0

    print("\nSolution 2 Results:")
    print(sol2.maxProfit(prices1))  # Output: 7
    print(sol2.maxProfit(prices2))  # Output: 4
    print(sol2.maxProfit(prices3))  # Output: 0
