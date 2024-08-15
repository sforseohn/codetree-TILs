n = int(input())
works = []

for i in range(n):
    t, p = map(int, input().split())
    works.append((t, p))

dp = [0] * n # 각 시점에서 가능한 최대 이익
dp[0] = works[0][1]

for i in range(1, n): # 각 시점마다
    if i + works[i][0] > n: # n일 내에 마무리되지 않으면 건너뛰기
        continue

    dp[i] = works[i][1] # 현 시점의 이익

    # 가능한 이전 시점의 최대 이익 가져오기
    for j in range(i):
        if j + works[j][0] <= i: 
            dp[i] = max(dp[i], works[i][1] + dp[j])

print(max(dp))