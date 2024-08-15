n = int(input())
values = [7, 5, 2, 1]

cnt = 0
for value in values:
    if value == 0:
        break
        
    cnt += n // value
    n %= value

print(cnt)