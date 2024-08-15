n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
same_cnt = 1

# 가로
for i in range(n):
    for j in range(1, n):
        if grid[i][j] == grid[i][j-1]:
            same_cnt += 1
        else:
            same_cnt = 1
        
        if same_cnt == m:
            cnt += 1
            break

# 세로
for j in range(n):
    for i in range(1, n):
        if grid[i][j] == grid[i-1][j]:
            same_cnt += 1
        else:
            same_cnt = 1
        
        if same_cnt == m:
            cnt += 1
            break

if m == 1:
    print(n*2)
else:
    print(cnt)