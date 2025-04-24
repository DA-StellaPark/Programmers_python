def solution(num_list):
    result =eval('*'.join([str(n) for n in num_list]))
    result2 = sum(num_list)**2
    answer = 1 if result < result2 else 0
    return answer