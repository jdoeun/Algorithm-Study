import heapq

def solution(n, works):
    answer = 0
    
    if sum(works) <= n:
        return answer
    else:
        works = [-i for i in works]
        heapq.heapify(works)
        
        while(n > 0):
            heapq.heappush(works, heapq.heappop(works) + 1)
            n -= 1
        
        for i in works:
            answer += i ** 2
    
    
    return answer