"""
Problem: Best Time to Buy and Sell Stock
Difficulty: Easy

You are given an array 'prices' where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input Format:
- prices: List[int] where 1 <= len(prices) <= 10^5 and 0 <= prices[i] <= 10^4

Output Format:
- Integer representing the maximum profit obtainable

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No profitable transaction is possible.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""

# ===============================
# Solution 1: Using Python built-in functions (HackerRank style)
# ===============================

from typing import List  # Import List for type hinting

class SolutionBuiltIn:
    def maxProfit(self, prices: List[int]) -> int:
        """
        This solution uses Python's built-in min() and max() functions to track
        the minimum price seen so far and maximum profit.
        """

        # Initialize minimum price as infinity so the first price will automatically be smaller
        min_price = float('inf')
        # Initialize maximum profit as zero (no transaction gives zero profit)
        max_profit = 0

        # Loop over each price in the list
        for price in prices:
            # Update the minimum price if current price is smaller
            min_price = min(min_price, price)
            # Compute potential profit if sold at current price after buying at min_price
            profit = price - min_price
            # Update maximum profit if the current profit is larger
            max_profit = max(max_profit, profit)

        # Return the maximum profit found
        return max_profit

# Time Complexity Analysis:
# - Loop iterates through 'n' prices once -> O(n)
# - min() and max() here are used on two numbers only (not a list) -> O(1) each
# Overall time complexity: O(n)
#
# Space Complexity Analysis:
# - We only store min_price, max_profit, and profit -> O(1) constant space
# - No extra data structures proportional to input size
# Overall space complexity: O(1)


# ===============================
# Solution 2: Manual implementation without built-ins
# ===============================

class SolutionManual:
    def maxProfit(self, prices: List[int]) -> int:
        """
        This solution manually tracks minimum price and maximum profit without using
        built-in min() or max() functions.
        """

        # Initialize minimum price to positive infinity to ensure first element sets it
        min_price = float('inf')
        # Initialize maximum profit to 0
        max_profit = 0

        # Iterate through each price in the list
        for price in prices:

            # Check if current price is less than minimum price seen so far
            if price < min_price:
                # Update minimum price to current price
                min_price = price

            # Otherwise, compute potential profit if sold at current price
            elif price - min_price > max_profit:
                # Update maximum profit if this potential profit is greater
                max_profit = price - min_price

        # After checking all prices, return the maximum profit found
        return max_profit

# Time Complexity Analysis:
# - Single loop over 'n' prices -> O(n)
# - Only constant time operations inside loop -> O(1) per iteration
# Overall time complexity: O(n)
#
# Space Complexity Analysis:
# - Only stores min_price and max_profit -> O(1)
# Overall space complexity: O(1)


# ===============================
# Example Run
# ===============================

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]

    # Using built-in functions
    solution1 = SolutionBuiltIn()
    print("Built-in Solution Output:", solution1.maxProfit(prices))  # Expected: 5

    # Using manual tracking
    solution2 = SolutionManual()
    print("Manual Solution Output:", solution2.maxProfit(prices))   # Expected: 5


