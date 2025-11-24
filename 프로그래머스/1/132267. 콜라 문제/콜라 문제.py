def solution(a, b, n):
    answer = 0
    while n >= a:
        exchanged = (n // a) * b # 마트에서 받은 콜라 수
        n = exchanged + (n % a) # 받은 콜라 + 남은 콜라 = 갖고있는 콜라 수
        answer += exchanged # 받은 갯수 합치기
    return answer