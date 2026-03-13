def solution(progresses, speeds):
    answer = []
    days = []

    # 기간 구하기
    for i in range(len(progresses)):
        days.append((100 - progresses[i] + speeds[i]-1) // speeds[i])
    print(days)

    # 기능 배포 개수
    current = days[0]
    count = 1
    for i in range(1, len(days)):
        if days[i] <= current:
            count += 1
        else:
            answer.append(count)
            count = 1
            current = days[i]

    # 마무리 기능 배포
    answer.append(count)




    return answer