def solution(n):
    answer = 0
    for _ in range(n): # 변수 필요 없을떄 _ 사용
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer