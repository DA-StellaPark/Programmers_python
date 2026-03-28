def solution(ingredient):
    stack = []
    answer = 0
    target = [1, 2, 3, 1]  # 햄버거 패턴

    for item in ingredient:
        stack.append(item)  # 스택에 재료를 추가
        # 스택 길이가 4 이상일 때만 슬라이싱 수행
        if len(stack) >= 4 and stack[-4:] == target:
            answer += 1
            del stack[-4:]  # 햄버거 패턴 제거

    return answer