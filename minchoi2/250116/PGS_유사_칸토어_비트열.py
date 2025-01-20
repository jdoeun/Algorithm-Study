# 주어진 인덱스가 1인지 판단하는 함수
# 5진수로 표현했을 때, 어느 자리수라도 2가 포함되면 0을 반환
def is_one(l):
    while l >= 5:  # 현재 인덱스가 5 이상인 경우
        if (l - 2) % 5 == 0:  # 5로 나눈 나머지가 2인 경우 (중앙 영역)
            return False  # 0에 해당하므로 False 반환
        l //= 5  # 5로 나누어 상위 단계로 이동
    return l != 2  # 최종적으로 l이 2면 0, 아니면 1

# 주어진 n번째 유사 칸토어 비트열에서 [l, r] 구간의 1의 개수를 계산하는 함수
def solution(n, l, r):
    answer = 0  # 1의 개수를 저장할 변수 초기화
    for idx in range(l - 1, r):  # l-1 ~ r-1 (0-based index)
        if is_one(idx):  # 현재 인덱스가 1인지 확인
            answer += 1  # 1이면 개수 증가
    return answer  # 최종적으로 1의 개수 반환
