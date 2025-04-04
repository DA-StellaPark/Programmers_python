def solution(n):
    answer = [odd for odd in range(1, n + 1) if odd % 2 != 0]
    return answer