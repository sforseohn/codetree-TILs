n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0
for i in range(len(grid) - 3 + 1):
    for j in range(len(grid) - 3 + 1):
        cnt = 0
        for x in range(3):
            for y in range(3):
                cnt += grid[i + x][j + y]

        max_cnt = max(max_cnt, cnt)

print(max_cnt)