def solution(scores):
    target = scores[0]
    valid = []

    scores.sort(key=lambda x: (-x[0], x[1]))
    cmp_value = scores[0][1]

    for i in range(len(scores)):
        if scores[i][1] >= cmp_value:
            valid.append(scores[i])
            cmp_value = scores[i][1]
        else:
            if scores[i] == target:
                return -1

    valid.sort(key=lambda x: sum(x), reverse=True)
    scores_sum = [sum(x) for x in valid]

    rank = [1] * len(scores_sum)
    same = 1

    for i in range(1, len(scores_sum)):
        if scores_sum[i] == scores_sum[i - 1]:
            rank[i] = rank[i - 1]
            same += 1
        elif scores_sum[i] < scores_sum[i - 1]:
            rank[i] = rank[i - 1] + same
            same = 1

    for i in range(len(scores_sum)):
        if scores_sum[i] == sum(target):
            return rank[i]


# 참고한 풀이
def solution(scores):
    answer = 0
    target_a, target_b = scores[0]
    target_score = target_a + target_b

    scores.sort(key=lambda x: (-x[0], x[1]))

    maxb = 0

    for a, b in scores:
        if target_a < a and target_b < b:
            return -1
        if b >= maxb:
            maxb = b
            if a + b > target_score:
                answer += 1

    return answer + 1

