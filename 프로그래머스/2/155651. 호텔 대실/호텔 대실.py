def to_minutes(time): # 분으로 통일
    h, m = map(int, time.split(':'))
    return h * 60 + m 

def solution(book_time):
    rooms = []
    books = sorted([
        (to_minutes(start), to_minutes(end) + 10) # 청소시간까지 추가
        for start, end in book_time
        ])

    for start, end in books:
        for i in range(len(rooms)):
            if rooms[i] <= start:
                rooms[i] = end
                break
        else:
            rooms.append(end)
            
        rooms.sort()

    return len(rooms)