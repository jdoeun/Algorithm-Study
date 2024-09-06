def solution(k, tangerine):
    answer = 0
    length = max(tangerine) + 1
    
    info = [0] * length
    
    for i in range(len(tangerine)):
        info[tangerine[i]] += 1
        
    info.sort(reverse = True)
        
    for i in range(length):
        if k <= info[i]:
            answer += 1
            break
        else:
            k -= info[i]
            answer += 1

    return answer
