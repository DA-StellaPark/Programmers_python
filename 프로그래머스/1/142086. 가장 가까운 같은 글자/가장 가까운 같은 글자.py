def solution(s):
    answerList = [-1]*len(s)
    for i in range(len(s)):
        for j in range(i):
            if (s[i] == s[j]):
                answerList[i] = i-j          
    return answerList