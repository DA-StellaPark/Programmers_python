def solution(my_string, index_list):
    answer = ''
    for i in range(len(index_list)):
        answer += my_string[index_list[i]]
    return answer

# return ''.join([my_string[idx] for idx in index_list])