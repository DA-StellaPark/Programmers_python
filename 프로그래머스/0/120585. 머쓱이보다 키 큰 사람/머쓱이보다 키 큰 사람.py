def solution(array, height):
    answer = len([i for i in array if height<i])
    return answer