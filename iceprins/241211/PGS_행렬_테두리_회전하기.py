def solution(rows, columns, queries):
    answer = []

    arr = [[0 for _ in range(columns)] for _ in range(rows)]

    n = 1

    for i in range(rows):
        for j in range(columns):
            arr[i][j] = n
            n += 1

    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        num = arr[x1][y2]
        ans = num
        for i in range(y2 - 1, y1 - 1, -1):
            tmp = arr[x1][i]
            arr[x1][i + 1] = tmp
            ans = min(ans, tmp)
        for i in range(x1 + 1, x2 + 1):
            tmp = arr[i][y1]
            arr[i - 1][y1] = tmp
            ans = min(ans, tmp)
        for i in range(y1 + 1, y2 + 1):
            tmp = arr[x2][i]
            arr[x2][i - 1] = tmp
            ans = min(ans, tmp)
        for i in range(x2 - 1, x1 - 1, -1):
            tmp = arr[i][y2]
            arr[i + 1][y2] = tmp
            ans = min(ans, tmp)

        arr[x1 + 1][y2] = num
        answer.append(ans)

    return answer

