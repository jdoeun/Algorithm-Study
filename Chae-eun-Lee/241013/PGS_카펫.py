def solution(brown, yellow):
    #노란 격자가 일자인 경우
    # if brown == (yellow*2 + 6):
    #     return [yellow+2, 3]
    # else:
    oneside = (brown-4)//2
    for i in range(1, oneside//2+1):
        if i*(oneside-i) == yellow:
            return [(oneside-i+2), i+2]