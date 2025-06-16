def solution(array, n):
    array.sort()
    temp = []
    for i in array :
        temp.append(abs(n-i))
    return array[temp.index(min(temp))]
#solution = lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]