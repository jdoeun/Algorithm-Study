def solution(citations):
    left, right = 0, 10000

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for c in citations:
            if c >= mid:
                cnt += 1
        if cnt >= mid:
            left = mid + 1
        else:
            right = mid - 1

    return right

