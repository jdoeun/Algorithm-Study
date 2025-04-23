def get_exact_length(digit_num):
    for i in range(50):
        result = 2 ** (i + 1) - 1
        if result >= digit_num:
            return result


def is_valid(binary):
    def check(sub):
        if len(sub) == 1:
            return True
        mid = len(sub) // 2
        root = sub[mid]
        left = sub[:mid]
        right = sub[mid + 1:]
        if root == "0" and ("1" in left + right):
            return False
        return check(left) and check(right)

    return check(binary)


def solution(numbers):
    answer = []

    for number in numbers:
        bin_num = bin(number)[2:]
        exact_length = get_exact_length(len(bin_num))
        bin_num = bin_num.zfill(exact_length)

        if is_valid(bin_num):
            answer.append(1)
        else:
            answer.append(0)

    return answer

