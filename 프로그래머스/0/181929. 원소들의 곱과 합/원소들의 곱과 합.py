def solution(num_list):
    result = 1
    for num in num_list:
        result *= num
    result2 = sum(num_list)**2
    answer = 1 if result < result2 else 0
    return answer