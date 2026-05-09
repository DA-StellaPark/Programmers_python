
2
3
4
5
6
def solution(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, (a + b) % 1000000007
    return b