import heapq


def solution(operations):
    heap = []

    for op in operations:
        command, number = op.split(" ")
        number = int(number)
        if command == 'I':
            heapq.heappush(heap, number)
        else:
            if heap:
                if number == 1:
                    heap.sort()
                    heap.pop()
                else:
                    heapq.heappop(heap)

    heap.sort()

    if not heap:
        return [0, 0]

    return [heap[-1], heap[0]]
