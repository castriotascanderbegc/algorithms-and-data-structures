"""
    Q: Given a list of N items, and a backpack with a limited capacity, 
    return the maximum total profit that can be contained in the backpack. 
    The i-th item's profit is profit[i] and its weight is weight[i]. 
    Assume you can only add each item to the bag at most once.

"""


# Brute Force Solution
# Recursive approach 
# Time Complexity: O(2^n), Space: O(n), where n: number of items

def dfs(profit, weight, capacity):
    return dfsHelper(0, profit, weight, capacity)

def dfsHelper(i, profit, weight, capacity):
    if i == len(profit):
        return 0

    # Decide to skip item i
    maxProfit = dfsHelper(i + 1, profit, weight, capacity)

    # Decide to include item i
    newCapacity = capacity - weight[i]
    # Make sure new capacity does not overflow
    if newCapacity >= 0:
        currentProfit = profit[i] + dfsHelper(i + 1, profit, weight, newCapacity)
        
        # Compute the maximum profit
        maxProfit = max(maxProfit, currentProfit)
    
    return maxProfit


# Memoization Solution
# Using a cache to store the computed values so we don't have to recompute them
# Time Complexity: T(n): O(n • m) where n: number of items & m: capacity

def memoization(profit, weight, capacity):
    # We need a 2D grid with N rows and M + 1 columns
    N, M = len(profit), capacity
    # We can initiailize the grid with all -1s
    cache = [[-1] * (M + 1) for _ in range(N)]
    return memoHelper(0, profit, weight, capacity, cache)

def memoHelper(i, profit, weight, capacity, cache):
    if i == len(profit):
        return 0 
    # if profit has already been calculated for item i, read it from cache 
    if cache[i][capacity] != -1:
        return cache[i][capacity]
    
    # Decide to skip item i
    cache[i][capacity] = memoHelper(i + 1, profit, weight, capacity, cache)

    # new capacity
    newCapacity = capacity - weight[i]

    # Make sure newCapacity does not overflow
    # Decide to include item i
    if newCapacity >= 0:
        currentProfit = profit[i] + memoHelper(i + 1, profit, weight, newCapacity, cache)
        
        # Compute maximum profit
        cache[i][capacity] = max(currentProfit, cache[i][capacity])

    return cache[i][capacity]


# Dynamic Programming Solution
# Time: O(n • m), Space: O(n • m)

def dp(profit, weight, capacity):
    N, M = len(profit), capacity
    dp = [[0] * (M + 1) for _ in range(N)]

    # Fill the first column to reduce edge cases
    for i in range(N):
        # Cannot use column 0, as we don't have enough capacity, i.e. 0 capacity
        dp[i][0] = 0
    
    # Fill the first row to reduce edge cases
    for c in range(M + 1):
        # if weight at row = 0 is within capacity, add the profit
        if weight[0] <= c:
            dp[0][c] = profit[0]
    
    # Start from row = 1, and look up if needed
    for i in range(1, N):
        # Start from col = 1, and look to the left if needed
        for c in range(1, M + 1):
            skip = dp[i - 1][c]     # value at row above, if we don't include it
            include = 0
            # if new capacity does not overflow, we want to include it
            if c - weight[i] >= 0:
                include = profit[i] + dp[i - 1][c - weight[i]]
            
            dp[i][c] = max(include, skip)
    
    # result will be right most cell
    return dp[N - 1][M]


# Memory Optimized Dynamic Programming Solution
# Time: O(n • m), Space: O(m)

def optimizedDP(profit, weight, capacity):
    N, M = len(profit), capacity
    dp = [0] * (M + 1)

    # Fill the first row to reduce edge cases
    for c in range(M + 1):
        if weight[0] <= c:
            dp[c] = profit[0]

    for i in range(1, N):
        currRow = [0] * (M + 1)
        for c in range(1, M + 1):
            skip = dp[c]
            include = 0
            if c - weight[i] >= 0:
                include = profit[i] + dp[c - weight[i]]
            currRow[c] = max(include, skip)
        dp = currRow
    
    return dp[M]