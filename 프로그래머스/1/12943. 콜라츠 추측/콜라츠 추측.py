def solution(n):
    for i in range(500):
        if n == 1:
            return i
        
        n = n // 2 if n % 2 == 0 else n * 3 + 1
        if n == 1:
            return i+1
        
    return -1 # 500 다끝날때까지 안나오면