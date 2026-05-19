def solution(arr, k):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
        if len(result) == k:
            break

    return result + [-1] * (k - len(result)) # 나머지 값 전부 -1로 채우기