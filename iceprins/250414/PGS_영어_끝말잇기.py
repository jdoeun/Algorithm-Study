def solution(n, words):
    answer = [0, 0]
    record = [words[0]]
    idx = 1
    m = len(words)

    while True:
        if words[idx % m] in record:
            return [idx % n + 1, idx // n + 1]
        if idx == len(words) - 1:
            return answer
        if words[idx % m][0] != words[(idx - 1) % m][-1]:
            return [idx % n + 1, idx // n + 1]
        record.append(words[idx % m])
        idx += 1

