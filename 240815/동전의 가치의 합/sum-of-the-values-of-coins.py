def findMinCoin(n):
    coins = [1, 2, 5, 7]
    
    INF = float('inf')
    dp = [INF] * (n + 1)
    
    # 0원부터 시작
    dp[0] = 0
    
    for i in range(1, n+1):
        for coin in coins:
            if i - coin >= 0: # 동전을 사용할 수 있으면
                dp[i] = min(dp[i-coin] + 1, dp[i])
    
    return dp[n]


n = int(input())

print(findMinCoin(n))