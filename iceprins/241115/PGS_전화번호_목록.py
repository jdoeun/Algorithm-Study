# 풀이 1
def solution(phone_book):
    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False

    return True


# 풀이 2
def solution(phone_book):
    hash_map = {}

    for num in phone_book:
        hash_map[num] = 1

    for nums in phone_book:
        arr = ""
        for num in nums:
            arr += num

            if arr in hash_map and arr != nums:
                return False

    return True

