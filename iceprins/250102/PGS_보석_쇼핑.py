from collections import defaultdict


def solution(gems):
    answer = [0, len(gems) - 1]
    n = len(set(gems))

    stats = defaultdict(int)
    left, right = 0, 0

    stats[gems[0]] += 1

    while left < len(gems) and right < len(gems):
        if n == len(stats):
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            else:
                stats[gems[left]] -= 1
                if stats[gems[left]] == 0:
                    del stats[gems[left]]
                left += 1
        elif n > len(stats):
            right += 1

            if right == len(gems):
                break

            stats[gems[right]] += 1

    return [answer[0] + 1, answer[1] + 1]

