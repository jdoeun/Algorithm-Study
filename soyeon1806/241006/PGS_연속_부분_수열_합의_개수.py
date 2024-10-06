def solution(elements):
    answer = set()
    
    elementsLen = len(elements)
    elements = elements * 2
    
    for i in range(elementsLen):
        for j in range(elementsLen):
            answer.add(sum(elements[j : j + i]))
    
    return len(answer)