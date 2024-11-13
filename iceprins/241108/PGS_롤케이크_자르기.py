from collections import Counter


def solution(topping):
    answer = 0

    left = Counter(topping)
    right = {}

    for i in range(len(topping)):
        if topping[i] in right:
            right[topping[i]] += 1
        else:
            right[topping[i]] = 1

        left[topping[i]] -= 1

        if not left[topping[i]]:
            del (left[topping[i]])

        if len(left) == len(right):
            answer += 1

    return answer

