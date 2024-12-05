def solution(n, stations, w):
    answer = 0
    scope = 2 * w + 1
    start = 1

    for station in stations:
        if station - w - start > 0:
            answer += (station - w - start) // scope
            if (station - w - start) % scope != 0:
                answer += 1
        start = station + w + 1

    if n - start + 1 > 0:
        answer += (n - start + 1) // scope
        if (n - start + 1) % scope:
            answer += 1

    return answer

