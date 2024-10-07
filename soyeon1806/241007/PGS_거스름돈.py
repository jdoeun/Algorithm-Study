def solution(n, money):
    cache = [[0 for i in range(n+1)] for j in range(len(money))]
    
    cache[0][0] = 1

    for i in range(money[0],n+1,money[0]):
        cache[0][i] = 1
    for i in range(1, len(money)):
        for j in range(n+1):
            if j < money[i]:
                cache[i][j] = cache[i-1][j]
            else:
                cache[i][j] = (cache[i-1][j] + cache[i][j-money[i]])%1000000007
    return cache[len(money)-1][n]
