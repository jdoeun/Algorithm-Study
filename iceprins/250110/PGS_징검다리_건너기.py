def solution(stones, k):
    start = 1
    end = 200000000

    while start <= end:
        mid = (start + end) // 2
        copy_stones = stones.copy()

        tmp = 0

        for stone in copy_stones:
            if stone - mid <= 0:
                tmp += 1
            else:
                tmp = 0
            if tmp >= k:
                break

        if tmp >= k:
            end = mid - 1
        else:
            start = mid + 1

    return start

