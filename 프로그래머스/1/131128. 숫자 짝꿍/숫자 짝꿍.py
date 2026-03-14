from collections import Counter

def solution(X, Y):
    # 각 숫자의 등장 횟수
    count_X = Counter(X)
    count_Y = Counter(Y)
    
    result = []

    # 9부터 0까지 공통 숫자 확인 (큰 숫자부터 추가하기 위함)
    for digit in map(str, range(9, -1, -1)):
        common_count = min(count_X[digit], count_Y[digit])
        result.extend([digit] * common_count)

    # 공통 숫자가 하나도 없으면 -1 반환
    if not result:
        return "-1"

    answer = ''.join(result)

    # 결과가 0으로만 이루어져 있으면 "0" 반환
    return "0" if answer[0] == '0' else answer