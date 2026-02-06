def solution(babbling):
    speak = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        prev = ""
        i = 0
        success = True

        while i < len(word):
            matched = False
            for s in speak:
                # 현재 위치부터 s 길이만큼 단어가 s와 같고, 이전 음절과 같지 않을 때
                if word[i:i+len(s)] == s and s != prev:
                    prev = s
                    i += len(s)
                    matched = True
                    break
            if not matched:
                success = False
                break

        if success:
            count += 1

    return count