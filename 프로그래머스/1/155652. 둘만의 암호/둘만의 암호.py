def solution(s, skip, index):
    import string
    
    # 사용할 수 있는 알파벳 (skip 제외)
    alpabets = [c for c in string.ascii_lowercase if c not in skip]

    answer = ''
    for c in s:
        # 현재 문자의 위치
        pos = alpabets.index(c)
         # index만큼 이동 (순환)
        char = alpabets[(pos+index)%len(alpabets)]
        answer += char
    
    return answer