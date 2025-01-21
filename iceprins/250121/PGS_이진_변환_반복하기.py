def solution(s):
    cnt_transform, cnt_remove = 0, 0

    while True:
        if s == "1":
            break

        if "0" in s:
            cnt_remove += s.count("0")
            s = s.replace("0", "")
        length = len(s)
        s = str(bin(length))[2:]
        cnt_transform += 1

    return [cnt_transform, cnt_remove]

