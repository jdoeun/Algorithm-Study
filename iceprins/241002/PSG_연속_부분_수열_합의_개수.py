def solution(elements):
    size = len(elements)
    dp = [[0] * size for _ in range(size)]

    nums = set()

    for i in range(size):
        dp[0][i] = elements[i]

    for i in range(1, size):
        for j in range(size):
            dp[i][j] = dp[i - 1][j] + elements[(j + i) % size]

    for i in range(size):
        nums = nums.union(set(dp[i]))

    return len(nums)
