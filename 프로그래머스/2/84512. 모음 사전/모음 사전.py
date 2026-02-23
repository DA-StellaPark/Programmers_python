import itertools

def solution(word):
    answer = 0
    letter = ['A', 'E', 'I', 'O','U']
    combi = []
    for i in range(1, 6):
        combi += list(itertools.combinations_with_replacement((letter), i))

    combi.sort()
    perm = []
    for c in combi:
        perm += list(set(list(itertools.permutations(c))))

    w = tuple(word)
    perm.sort()

    print(len(perm))
    return perm.index(w) +1





