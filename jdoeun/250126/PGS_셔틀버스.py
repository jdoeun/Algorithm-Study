def solution(n, t, m, timetable):
    answer = 0

    # 모든 시간을 분으로 환산해서 생각 -> 계산 용이

    # 크루 도착 시각 리스트
    crewTime = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    crewTime.sort()

    # 버스 도착 시각 리스트 (9시부터~)
    busTime = [9*60 + t*i for i in range(n)]

    i = 0 # 다음에 버스에 오를 크루의 인덱스

    for tm in busTime:
        cnt = 0 # 버스에 타는 크루 수

        while (cnt < m # 버스에 자리가 남아있다
               and i < len(crewTime) # 탑승할 크루가 남아있다
               and crewTime[i] <= tm): # 해당 크루가 버스 도착 시간 전에 도착
            i += 1
            cnt += 1

        # 버스에 자리가 남았을 경우
        if cnt < m:
            answer = tm

        # 버스에 자리가 없는 경우 맨 마지막 크루보다 1분 먼저 도착
        else:
            answer = crewTime[i - 1] - 1

    # zfill로 최소 길이 2로 맞추어 출력
    return str(answer//60).zfill(2) + ":" + str(answer % 60).zfill(2)
