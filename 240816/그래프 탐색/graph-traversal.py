def dfs(v):
    global cnt
    for next in range(1, n+1):
        if graph[v][next] and not visited[next]:
            cnt += 1
            visited[next] = True
            dfs(next)

# 입력
n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

# 연산
visited = [False] * (n+1)
visited[1] = True

cnt = 0
dfs(1)

# 출력
print(cnt)