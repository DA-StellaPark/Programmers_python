def solution(my_string, is_suffix):
    answer = 1 if my_string[-len(is_suffix):] == is_suffix else 0
    return answer