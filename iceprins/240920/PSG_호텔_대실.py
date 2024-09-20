import heapq


def solution(book_time):
    for x in book_time:
        start, end = x[0], x[1]

        tmp1 = list(map(int, start.split(":")))
        tmp2 = list(map(int, end.split(":")))

        start = tmp1[0] * 60 + tmp1[1]
        end = tmp2[0] * 60 + tmp2[1]

        x[0], x[1] = start, end

    book_time.sort()
    q = []

    for i in range(len(book_time)):
        start, end = book_time[i][0], book_time[i][1]
        if not q:
            heapq.heappush(q, end)
            continue
        tmp = heapq.heappop(q)
        if tmp + 10 > start:
            heapq.heappush(q, tmp)
            heapq.heappush(q, end)
        else:
            heapq.heappush(q, end)

    return len(q)
