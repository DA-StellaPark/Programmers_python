def solution(n):
    output = 0
    for i in range(4, n + 1): # 3 이하는 소수, 4부터
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output