def solution(n):
    count = 0                      
    for i in range(1, n+1):         # 15=15
        suml = 0                     
        for j in range(i, n+1):     
            suml += j               
            if suml == n:           # 더한 값이(sumN)이 n과 같다면 count +1, break
                count += 1          
                break
            if suml > n:            # 더한 값(sumN)이 n보다 크다면 계산할 필요가 없음
                break
    return count