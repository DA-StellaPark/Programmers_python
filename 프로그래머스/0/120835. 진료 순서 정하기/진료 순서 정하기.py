def solution(emergency):
    answer = [sorted(emergency, reverse=True).index(x)+1 for x in emergency]
    return answer