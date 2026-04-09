from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    # S, L, E 한 번에 찾기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                S = (i, j)
            elif maps[i][j] == 'L':
                L = (i, j)
            elif maps[i][j] == 'E':
                E = (i, j)

    def bfs(start, target):
        queue = deque([(start[0], start[1], 0)])
        visited = [[False]*m for _ in range(n)]
        visited[start[0]][start[1]] = True
        
        while queue:
            x, y, d = queue.popleft()
            if (x, y) == target:
                return d
            
            for nx, ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and maps[nx][ny] != 'X':
                        visited[nx][ny] = True
                        queue.append((nx, ny, d+1))
        return -1

    d1 = bfs(S, L)
    if d1 == -1:
        return -1
    
    d2 = bfs(L, E)
    return d1 + d2 if d2 != -1 else -1