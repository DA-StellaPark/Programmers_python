def solution(num, k):
    strnum = str(num)
    if str(k) in strnum:
        answer = strnum.index(str(k))+1
    else:
        answer = -1
    return answer