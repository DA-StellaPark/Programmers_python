def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5] * 2000
    second = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    ans_1 = 0
    ans_2 = 0
    ans_3 = 0
    for i in range(len(answers)):
        if first[i] == answers[i]:
            ans_1 += 1

        if second[i] == answers[i]:
            ans_2 += 1

        if third[i] == answers[i]:
            ans_3 += 1

    if ans_1 > ans_2 and ans_1 > ans_3:
        answer.append(1)
    elif ans_2 > ans_1 and ans_2 > ans_3:
        answer.append(2)
    elif ans_3 > ans_1 and ans_3 > ans_2:
        answer.append(3)
    elif ans_1 == ans_2 and ans_1 > ans_3:
        answer = [1, 2]
    elif ans_1 == ans_3 and ans_1 > ans_2:
        answer = [1, 3]
    elif ans_2 == ans_3 and ans_2 > ans_1:
        answer = [2, 3]
    else:
        answer = [1, 2, 3]
    return answer