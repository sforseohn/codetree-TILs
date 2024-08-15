n = int(input())
nums = list(map(int, input().split()))

left = right = 0
max_range = 1

while right < n - 1:
    right += 1

    if nums[right] == nums[left]: # 중복 발생
        left += 1

    current_range = right - left + 1
    max_range = max(max_range, current_range)

print(max_range)