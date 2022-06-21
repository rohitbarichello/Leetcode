def climbStairs(n):
    numWays = [0, 1, 2]
    
    if n > 2:
        for i in range(3, n + 1):
            numWays.append(numWays[i - 1] + numWays[i - 2])
    
    return numWays[n]