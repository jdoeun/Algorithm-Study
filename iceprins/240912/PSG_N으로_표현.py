def solution(N, number):
    if N == number:
        return 1

    dp = [set() for _ in range(9)]
    dp[1].add(N)

    for i in range(2, 9):
        for j in range(1, i):
            first = dp[j]
            second = dp[i - j]
            for x in first:
                for y in second:
                    dp[i].add(int(str(N) * i))
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)

        if number in dp[i]:
            return i

    return -1
