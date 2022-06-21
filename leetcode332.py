def coinChange(coins, amount):
    # num coins is value and index is amount
    
    minNumCoins = [0]
    for i in range(1, amount + 1):
        minNumCoins.append(float('inf'))

        for coin in coins:
            if i - coin >= 0:
                minNumCoins[i] = min(minNumCoins[i], minNumCoins[i - coin] + 1)
    
    if minNumCoins[-1] == float("inf"):
        return -1
    else:
        return minNumCoins[-1]