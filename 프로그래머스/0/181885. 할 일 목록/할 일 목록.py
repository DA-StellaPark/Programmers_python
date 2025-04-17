def solution(todo_list, finished):
    idx = [i for i, x in enumerate(finished) if x==False]
    return [todo_list[i] for i in idx]