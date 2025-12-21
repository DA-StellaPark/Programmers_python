from math import gcd # 최소공배수 구하는 함수

def solution(arr):
    answer = arr[0]                                 

    for num in arr:
        answer = answer*num // gcd(answer, num)     

    return answer