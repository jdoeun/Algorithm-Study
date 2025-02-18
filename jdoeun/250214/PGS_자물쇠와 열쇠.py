# 자물쇠와 열쇠 (구현)

# NxN 2차원 리스트 d도 회전
# 회전 각도 d => 1: 90도, 2: 180도, 3: 270도
def rotate(array, d):
    n = len(array)  # 배열의 크기
    result = [[0] * n for _ in range(n)]  # 회전 결과 저장용

    if d % 4 == 1:  # 90도 회전
        for r in range(n):
            for c in range(n):
                result[c][n - r - 1] = array[r][c]
    elif d % 4 == 2:  # 180도 회전
        for r in range(n):
            for c in range(n):
                result[n - r - 1][n - c - 1] = array[r][c]
    elif d % 4 == 3:  # 270도 회전
        for r in range(n):
            for c in range(n):
                result[n - c - 1][r] = array[r][c]
    else:  # 0도 (변경 없음)
        for r in range(n):
            for c in range(n):
                result[r][c] = array[r][c]

    return result



# 자물쇠 중간 NxN 부분이 모두 1인지 확인
# == 확장된 자물쇠(new_lock)의 중앙 부분이 모두 1인지 확인
def check(new_lock):
    n = len(new_lock) // 3 # 원래 자물쇠 크기
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if new_lock[i][j] != 1: # 중앙 부분이 1이 아닌 경우 실패
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)

    # 기존 자물쇠보다 3배 큰 자물쇠(0으로 초기화)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 새로운 자물쇠의 중앙 부분에 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]

    # key를 이동시키면서 lock에 맞춰보기
    # 열쇠를 (1, 1)부터 (N*2, N*2)까지 이동시키며 확인 (부분만 덮는 경우도 확인 위해 1부터)
    for i in range(1, n * 2):
        for j in range(1, n * 2):

            # 열쇠를 0, 90, 180, 270도로 회전시키며 확인
            for d in range(4):
                r_key = rotate(key, d)  # key를 d만큼 회전시킨 리스트

                # new_lock에 key 배치
                for x in range(m):
                    for y in range(m):
                        new_lock[i + x][j + y] += r_key[x][y]

                # 중앙 부분이 1로 채워졌는지 확인
                if check(new_lock):
                    return True

                # key 배치한 부분 원상 복구
                for x in range(m):
                    for y in range(m):
                        new_lock[i + x][j + y] -= r_key[x][y]

    return False # 모든 경우 탐색 후에도 맞지 않으면 False 반환