def solution(word):
    answer = []

    def dfs(s, order):
        if s == word:
            answer.append(order)
        if len(s) == 5:
            return order
        for x in ['A', 'E', 'I', 'O', 'U']:
            order = dfs(s + x, order + 1)

        return order

    dfs("", 0)

    return answer[0]
