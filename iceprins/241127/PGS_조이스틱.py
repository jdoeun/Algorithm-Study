def solution(name):
    answer = 0
    
    min_move = len(name) - 1
    
    for i in range(len(name)):
        opt_1 = ord(name[i]) - ord('A')
        opt_2 = ord('A') - ord(name[i]) + 26
        answer += min(opt_1, opt_2)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min([min_move, 2 * i + (len(name) - next), 2 * (len(name) - next) + i])
    
    answer += min_move
    
    return answer

