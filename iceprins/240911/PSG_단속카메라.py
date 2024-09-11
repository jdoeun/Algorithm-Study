def solution(routes):
    answer = 1

    routes.sort(key=lambda x: x[1])
    pos = routes[0][1]

    for route in routes:
        if not route[0] <= pos <= route[1]:
            pos = route[1]
            answer += 1

    return answer
