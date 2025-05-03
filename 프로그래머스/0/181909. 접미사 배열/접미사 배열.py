def solution(my_string):
    result = []
    for i in range(len(my_string)):
        str = my_string[i:]
        result.append(str)
    result.sort()
    return result