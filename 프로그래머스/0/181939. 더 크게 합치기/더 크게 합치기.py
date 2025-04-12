def solution(a, b):
    str1 = str(a) + str(b)
    str2 = str(b) + str(a)

    if (str1 < str2):
        answer = str2
    elif (str2 < str1):
        answer = str1
    else:
        answer = str1

    return int(answer)