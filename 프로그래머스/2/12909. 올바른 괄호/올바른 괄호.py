def solution(s):
    stack = list()
    for i in s:
        if i == '(':
            stack.append(i)

        if i == ')':
            try:
                stack.pop()
            except IndexError:
                return False

    return len(stack) == 0