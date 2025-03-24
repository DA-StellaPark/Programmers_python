def solution(angle):
    answer = 1 if 0<angle<90 else 2 if angle == 90 else 3 if 90<angle<180 else 4
    
    # answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer