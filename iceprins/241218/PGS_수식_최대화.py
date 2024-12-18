import re
from itertools import permutations


def solution(expression):
    answer = -1

    for case in permutations(["+", "-", "*"], 3):
        numbers = re.split(r'[+\-*]', expression)
        operators = [x for x in expression if x in "+-*"]
        for op in case:
            while op in operators:
                idx = operators.index(op)
                if op == "+":
                    result = int(numbers[idx]) + int(numbers[idx + 1])
                elif op == "-":
                    result = int(numbers[idx]) - int(numbers[idx + 1])
                elif op == "*":
                    result = int(numbers[idx]) * int(numbers[idx + 1])

                numbers[idx] = result
                numbers.pop(idx + 1)
                operators.pop(idx)

        answer = max(answer, abs(numbers[0]))

    return answer

