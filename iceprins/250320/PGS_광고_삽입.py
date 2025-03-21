def transform(s):
    tmp = list(map(int, s.split(":")))
    return tmp[0] * 3600 + tmp[1] * 60 + tmp[2]


def transform_to_time(n):
    h = str(n // 3600).zfill(2)
    m = str((n % 3600) // 60).zfill(2)
    s = str((n % 3600) % 60).zfill(2)
    return h + ":" + m + ":" + s


def solution(play_time, adv_time, logs):
    answer = 0

    play_time = transform(play_time)
    adv_time = transform(adv_time)

    record = [0] * (play_time + 1)

    for i in range(len(logs)):
        start, end = logs[i].split("-")
        start = transform(start)
        end = transform(end)
        record[start] += 1
        record[end] -= 1

    for i in range(1, len(record)):
        record[i] = record[i] + record[i - 1]
    for i in range(1, len(record)):
        record[i] = record[i] + record[i - 1]

    max_value = 0

    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if max_value < record[i] - record[i - adv_time]:
                max_value = record[i] - record[i - adv_time]
                answer = i - adv_time + 1
        else:
            if max_value < record[i]:
                max_value = record[i]
                answer = i - adv_time + 1

    return transform_to_time(answer)

