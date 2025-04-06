def solution(price):
    discount = 0.2 if price>=500000 else 0.1 if price>=300000 else 0.05 if price>=100000 else 0
    return int(price-(price*discount))