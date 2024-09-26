def solution(numbers, target):
    answer = 0

    def dfs(idx, s):
        nonlocal answer
        if idx == len(numbers):
            if s == target:
                answer += 1
            return

        dfs(idx + 1, s + numbers[idx])
        dfs(idx + 1, s - numbers[idx])

    dfs(0, 0)

    return answer
