def solution(sequence, k):
    answer = [0, len(sequence) - 1]

    left, right = 0, 0
    s = sequence[0]

    while True:
        if s < k:
            right += 1
            if right == len(sequence):
                break
            s += sequence[right]
        else:
            if s == k:
                if right - left < answer[1] - answer[0]:
                    answer = [left, right]
            s -= sequence[left]
            left += 1

    return answer
