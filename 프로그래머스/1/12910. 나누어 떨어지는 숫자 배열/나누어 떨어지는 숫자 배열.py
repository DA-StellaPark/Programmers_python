def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    return sorted(answer) if len(answer) != 0 else [-1]

#2
# def solution(arr, divisor): 
#     return sorted([n for n in arr if n%divisor == 0]) or [-1]