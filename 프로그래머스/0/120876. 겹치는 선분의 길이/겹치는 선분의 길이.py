def solution(lines):
    visit:list = [False for _ in range(200)]
    L:list = [[lines[i][0] + 100, lines[i][1] + 100] for i in range(3)]
    for i in range(3) :
        TEMP:list = [False for _ in range(200)]
        for j in range(L[i][0], L[i][1], 1) :
            TEMP[j] = True
        for j in range(L[(i+1) % 3][0], L[(i+1) % 3][1], 1) :
            if TEMP[j] :
                visit[j] = True
    answer = 0
    for i in range(200) :
        if visit[i] :
            answer += 1

    return answer