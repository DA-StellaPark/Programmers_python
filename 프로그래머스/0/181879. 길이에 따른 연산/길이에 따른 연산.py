def solution(num_list):
    answer = 1
    if len(num_list) >= 11 :
        answer = sum(num_list) 
    else:
        for num in num_list:
            answer *= num
    return answer

# from math import prod
# def solution(num_list):
#     return sum(num_list) if len(num_list)>=11 else prod(num_list)