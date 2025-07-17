def solution(arr):
    stk = []       # 결과를 저장할 빈 스택 리스트 초기화
    idx = 0        # arr 배열을 순회하기 위한 인덱스 변수

    # idx가 arr의 길이보다 작을 동안 반복
    while idx < len(arr):
        # 1) stk가 비어 있다면
        if len(stk) == 0:
            stk.append(arr[idx])  # arr[idx]를 stk에 추가
            idx += 1              # 다음으로 이동

        # 2) stk가 비어 있지 않고, 마지막 원소가 현재 arr[idx]보다 작다면
        elif stk[-1] < arr[idx]:
            stk.append(arr[idx])  # arr[idx]를 stk에 추가
            idx += 1              # 다음으로 이동

        # 3) stk가 비었지 않고, 마지막 원소가 현재 arr[idx]보다 크거나 같다면
        else:
            stk.pop()             # stk의 마지막 원소를 제거 (더 큰 값 유지)

    # 모든 arr 원소를 처리한 후 최종 stk 결과 반환
    return stk
