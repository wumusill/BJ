def solution(schedules, timelogs, startday):
    answer = 0

    for t1, log in zip(schedules, timelogs):        # 출근 희망 시간과 실제 출근 로그 순회 
        h1, m1 = str(t1)[:-2], str(t1)[-2:]         # 출근 희망 시간에서 시와 분 분리, index 활용하기 위해 문자화
        h1, m1 = int(h1), int(m1)                   # 크기 비교를 위해 정수화
        m1 += 10                                    # 10분 추가

        if m1 >= 60:                                # 10분을 추가했는데 60이 넘으면 시로 올림
            h1 += 1
            m1 -= 60

        for idx, t2 in enumerate(log):              # 실제 로그 순회
            if (startday + idx) % 7 in [0, 6]:      # 주말 로그는 무시
                continue
            h2, m2 = str(t2)[:-2], str(t2)[-2:]     # 실제 출근 로그에서 시와 분 분리
            h2, m2 = int(h2), int(m2)               # 크기 비교를 위해 정수화

            if h2 > h1:                             # 시가 크면 지각
                break
            elif h2 == h1 and m2 > m1:              # 시는 같은데 분이 크면 지각 
                break
        else:                                       # 종료 조건 없이 순회를 마치면 이벤트 당첨
            answer += 1

    return answer