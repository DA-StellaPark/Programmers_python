def solution(arr, k):
    if k%2 != 0:
        answer = [x * k for x in arr]
    else:
        answer = [x + k for x in arr]
    return answer
    # [i*k if k%2!=0 else i+k for i in arr]