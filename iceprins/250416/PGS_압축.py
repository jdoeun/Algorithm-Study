def solution(msg):
    answer = []

    dictionary = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                  'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
                  'X': 24, 'Y': 25, 'Z': 26}

    char = list(msg)
    d_num = 27
    flag = False

    while True:
        if flag:
            break
        for i in range(len(char), 0, -1):
            w = ''.join(char[0:i])
            if w in dictionary:
                answer.append(dictionary[w])
                char = char[i:]
                if char:
                    dictionary[w + char[0]] = d_num
                    d_num += 1
                else:
                    flag = True
                break

    return answer

