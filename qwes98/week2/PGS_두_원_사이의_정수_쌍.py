import math

def solution(r1, r2):
    answer = (r2-r1+1)*2
    for x in range(1, r2+1):
        y2 = math.floor(math.sqrt(r2**2-x**2))
        if x < r1:
            y1 = math.ceil(math.sqrt(r1**2-x**2))
            answer += (y2-y1+1)*4
        else:
            answer += (y2*2+1)*2
        
    return answer
