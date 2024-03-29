# https://school.programmers.co.kr/learn/courses/30/lessons/1844

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    res = bfs(0, 0, N, M, maps)
    return res


def bfs(si, sj, N, M, maps):
    visited = [[0] * M for _ in range(N)]
    q = []
    q.append((si, sj))
    visited[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        # 종료조건
        if ci == N - 1 and cj == M - 1:
            return visited[N - 1][M - 1]

        for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and maps[ni][nj] == 1:
                q.append((ni, nj))
                # 거리를 구하기 위해서 +1
                visited[ni][nj] = visited[ci][cj] + 1

    return -1


# maps	                                                            answer
# [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	        11
# [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	        -1