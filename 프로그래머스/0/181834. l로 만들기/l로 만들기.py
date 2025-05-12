def solution(myString):
    answer = ''
    for a in myString:
        if a < 'l':
            answer += 'l'
        else:
            answer += a
    return answer