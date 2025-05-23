def solution(order):
    answer = 0
    for i in str(order):
        if i in ('3','6','9'):
            answer += 1
    return answer

# return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))