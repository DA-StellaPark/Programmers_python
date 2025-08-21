def solution(myString, pat):
    if pat not in myString:
        return myString
    
    # 패턴이 나타나는 마지막 인덱스를 찾기
    index = myString.rfind(pat)
    
    # myString의 마지막 패턴이 시작되는 인덱스까지 자르기
    return myString[:index + len(pat)]  # +len(pat) 추가하여 패턴 포함