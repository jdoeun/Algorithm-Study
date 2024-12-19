from itertools import permutations
import re


def solution(user_id, banned_id):
    result = []

    for i in range(len(banned_id)):
        banned_id[i] = banned_id[i].replace("*", ".")

    for case in map(list, permutations(user_id, len(banned_id))):
        check = True
        for i in range(len(case)):
            if re.match(banned_id[i], case[i]) and (len(case[i]) == len(banned_id[i])):
                continue
            else:
                check = False
                break
        if check:
            if sorted(case) not in result:
                result.append(sorted(case))

    return len(result)

