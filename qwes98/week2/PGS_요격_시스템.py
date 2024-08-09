def solution(targets):
    answer = 0
    targets.sort(key=lambda x: [x[1], x[0]])
    
    e = 0
    for t_s, t_e in targets:
        if t_s >= e:
            answer += 1
            e = t_e
    return answer
