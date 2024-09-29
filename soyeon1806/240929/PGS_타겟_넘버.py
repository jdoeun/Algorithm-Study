def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    for num in numbers:
        tmp = []
        
        for leaf in leaves:
            tmp.append(leaf + num)
            tmp.append(leaf - num)
        
        leaves = tmp
        
    for leaf in leaves:
        if leaf == target:
            answer += 1
    
    return answer