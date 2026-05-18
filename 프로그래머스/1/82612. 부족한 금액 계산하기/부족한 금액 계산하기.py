def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        answer += price * i
    return answer - money if answer > money else 0


# 2
# def solution(price, money, count):
#     return max(0, price * (count+1) * count // 2 - money) 

# 부족한 금액이 0원일 경우 대비해서 max 이용