binary_count = 0
count_zero = 0

def solution(s):
    global count_zero
    global binary_count
    answer = []

    def binary(s):
        global count_zero
        global binary_count

        binary_count += 1
        count_zero += s.count("0")  # 0 개수 누적
        s = s.replace("0", "")  # 0 제거
        new_s = bin(len(s))[2:]  # 남은 길이를 이진수로 변환

        if new_s != "1":
            binary(new_s)

    binary(s)
    answer.append(binary_count)
    answer.append(count_zero)

    return answer