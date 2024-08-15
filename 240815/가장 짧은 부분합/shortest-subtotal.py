# 입력
n, s = map(int, input().split())
nums = list(map(int, input().split()))

# 연산
shortest_range = n + 1
for i in range(n-1):
    for j in range(i, n):
        cur_range = j - i + 1

        if cur_range >= shortest_range:
            break

        sum_val = 0
        for l in range(i, j + 1):
            sum_val += nums[l]

        if sum_val >= s:
            shortest_range = min(shortest_range, cur_range)
            break

# 출력
if shortest_range == n+1:
    print(-1) 
else:
    print(shortest_range)