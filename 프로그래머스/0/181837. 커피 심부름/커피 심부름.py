def solution(order):
    answer = sum([4500 if 'americano' in o else 5000 if 'latte' in o else 4500 for o in order])
    return answer