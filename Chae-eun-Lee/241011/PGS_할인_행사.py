def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)):
        possible = True
        if discount[i] in want:
            dc = discount[i:i + 10]
            for j in range(len(want)):
                if number[j] != dc.count(want[j]):
                    possible = False
                    break
            if possible:
                answer += 1

    return answer