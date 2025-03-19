def solution(n):
    answer = []

    def solve(num, f, t, aux):
        if num == 1:
            answer.append([f, t])
            return
        solve(num - 1, f, aux, t)
        solve(1, f, t, aux)
        solve(num - 1, aux, t, f)

    solve(n, 1, 3, 2)

    return answer

