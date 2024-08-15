# 입력
n, s = map(int, input().split())
nums = list(map(int, input().split()))

# 연산
shortest_range = n + 1
for i in range(n-1):
    j = i
    while (j < n):
        temp_sum = sum(nums[i:j+1])
        cur_range = j - i + 1

        if cur_range >= shortest_range:
            break

        if temp_sum >= s and cur_range < shortest_range:
            shortest_range = cur_range
            break
        j += 1

# 출력
if shortest_range == n+1:
    print(-1) 
else:
    print(shortest_range)