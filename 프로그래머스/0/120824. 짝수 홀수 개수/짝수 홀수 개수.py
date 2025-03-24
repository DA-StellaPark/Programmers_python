def solution(num_list):
    a = b = 0
    for n in num_list:
        if n%2==0:
            a += 1
        else:
            b += 1
    return a, b