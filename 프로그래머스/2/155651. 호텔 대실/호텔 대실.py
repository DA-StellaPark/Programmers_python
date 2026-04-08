def to_minutes(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m 

def solution(book_time):
    rooms = []

    books = sorted([(to_minutes(start), to_minutes(end) + 10) for start, end in book_time])


    for start, end in books:
        for i in range(len(rooms)):
            if rooms[i] <= start:
                rooms[i] = end
                break
        else:
            rooms.append(end)

        rooms.sort()

    return len(rooms)