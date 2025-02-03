from collections import defaultdict
from itertools import combinations as comb


def solution(orders, course):
    answer = []

    for c in course:
        stats = defaultdict(int)
        for order in orders:
            if len(order) < c:
                continue
            pairs = list(comb(order, c))
            for pair in pairs:
                s = []
                for char in pair:
                    s.append(char)
                s.sort()
                s = "".join(s)
                stats[s] += 1

        stats = dict(sorted(stats.items(), key=lambda x: x[1], reverse=True))

        menus = list(stats.keys())

        if not menus:
            continue

        n = stats[menus[0]]

        if n < 2:
            continue

        for menu in menus:
            if stats[menu] == n:
                answer.append(menu)

    return sorted(answer)

