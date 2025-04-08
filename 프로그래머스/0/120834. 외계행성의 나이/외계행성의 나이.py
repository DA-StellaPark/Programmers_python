def solution(age):
    age = str(age)
    alp = ['a','b','c','d','e','f','g','h','i','j']
    answer = ''.join(alp[int(i)] for i in age)
    return answer