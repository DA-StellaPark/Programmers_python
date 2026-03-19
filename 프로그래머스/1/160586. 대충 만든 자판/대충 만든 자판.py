def solution(keymap, targets):
    answer = []
    for word in targets : 
        # 만들 수 없는 단어
        if len(set(word) - set(list(''.join(keymap)))) : 
            answer.append(-1)

        # 만들 수 있는 단어
        else : 
            cnt = 0
            for w in word : 
                # 가능한 key에서 index를 반환 후 가장 적게 누른 값을 찾는다
                get_cnt = min([key.index(w)+1 for key in keymap if w in key])
                cnt += get_cnt
            answer.append(cnt)                
    return answer