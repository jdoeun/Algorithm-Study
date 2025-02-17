def solution(arr1, arr2):

    # 결과 행렬 크기 (arr1의 행 개수 * arr2의 열 개수)
    result = [[0]* len(arr2[0]) for _ in range(len(arr1))]

    # 행렬 곱셈 수행
    for i in range(len(arr1)): # arr1 행만큼 반복
        for j in range(len(arr2[0])): # arr2의 열만큼 반복
            for k in range(len(arr2)): # 곱셈 시 k 결정
                result[i][j] += arr1[i][k] * arr2[k][j]

    return result