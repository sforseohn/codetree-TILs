n = int(input())
nums = list(map(int, input().split()))

left = 0
max_range = 1
seen = set()

for right in range(n):
    new = nums[right]

    # 중복이 있다면 없을 때까지 왼쪽 포인터 증가
    while left <= right and new in seen: 
        seen.remove(nums[left])
        left += 1

    seen.add(new)

    current_range = right - left + 1
    max_range = max(max_range, current_range)

print(max_range)