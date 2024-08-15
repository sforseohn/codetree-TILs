# 입력
n, s = map(int, input().split())
nums = list(map(int, input().split()))

# 연산
shortest_range = n + 1
current_sum = 0
left = right = 0

while right < n:
    current_sum += nums[right]

    while current_sum >= s:
        shortest_range = min(shortest_range, right - left + 1)
        current_sum -= nums[left]
        left += 1

    right += 1

# 출력
if shortest_range == n+1:
    print(-1) 
else:
    print(shortest_range)