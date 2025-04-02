def solution(n):
    fa, fb = 0, 1

    for i in range(2, n + 1):
        fc = (fa + fb) % 1234567
        fa = fb
        fb = fc

    return fc

