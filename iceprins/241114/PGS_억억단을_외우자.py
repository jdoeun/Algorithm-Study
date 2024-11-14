def get_aliquots(n):
    aliquots = [0] * (n + 1)
    for i in range(1, int(n ** 0.5) + 1):
        aliquots[i * i] += 1
        # i를 약수로 갖는 가장 작은 수가 i * (i + 1)
        for j in range(i * (i + 1), n + 1, i):
            aliquots[j] += 2
    return aliquots


def solution(e, starts):
    aliquot_cnt = get_aliquots(e)

    freq = [0] * (e + 1)
    max_aliquot = e

    for i in range(e, 0, -1):
        if aliquot_cnt[i] >= aliquot_cnt[max_aliquot]:
            max_aliquot = i
        freq[i] = max_aliquot

    return [freq[s] for s in starts]

