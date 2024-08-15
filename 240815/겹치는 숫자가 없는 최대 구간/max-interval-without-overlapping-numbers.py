n = int(input())
nums = list(map(int, input().split()))

left = 0
max_range = 1
seen = set()

for right in range(n-1):
    new = nums[right]

    if not new in seen: # 아직 발견되지 않았으면 추가
        seen.add(new)
    else:               # 중복 발생
        while left <= right and new in seen:
            seen.remove(nums[left])
            left += 1

    current_range = right - left + 1
    max_range = max(max_range, current_range)

print(max_range)