def solution(cards):
    answer = []
    visited = [False] * (len(cards) + 1)

    for card in cards:
        if not visited[card]:
            tmp = []
            while card not in tmp:
                tmp.append(card)
                card = cards[card - 1]
                visited[card] = True

            answer.append(len(tmp))

    if answer[0] == len(cards):
        return 0

    answer.sort(reverse=True)

    return answer[0] * answer[1]

