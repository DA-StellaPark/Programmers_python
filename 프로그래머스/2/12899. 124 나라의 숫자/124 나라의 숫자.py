from collections import deque


def solution(n):
    answer = ''
    deq = deque()

    def to3(n):
        while n != 0:
            deq.appendleft(n % 3)
            n = n//3

    def to124():
        while 0 in deq:
            for i in range(1, len(deq)):
                if deq[i] == 0:
                    deq[i] = 4
                    if deq[i-1] == 4:
                        deq[i-1] = 2
                    elif deq[i-1] == 2:
                        deq[i-1] = 1
                    elif deq[i-1] == 1:
                        deq[i-1] = 0
            if deq[0] == 0:
                deq.popleft()
    to3(n)
    to124()

    for num in deq:
        answer += str(num)

    return answer