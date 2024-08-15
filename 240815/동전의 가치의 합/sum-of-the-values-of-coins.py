n = int(input())
values = [7, 5, 2, 1]

cnt = 0
for value in values:
    cnt += n // value
    n %= value

print(cnt)