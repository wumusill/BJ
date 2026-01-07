# 분과 초를 분리해서 연산하면 놓치는 경우의 수가 많고 복잡해짐
# 초로 다 통일해서 구현하는게 편하고 놓치는 경우의 수가 없음


# 오프닝 구간이면 자동으로 점프하는 함수
def jump_opening(op_start, op_end, s):
    opm1, ops1, opm2, ops2 = int(op_start.split(':')[0]), int(op_start.split(':')[1]), int(op_end.split(':')[0]), int(op_end.split(':')[1]) 
    
    a = opm1 * 60 + ops1
    c = opm2 * 60 + ops2
    
    if a <= s <= c:
        return c
    return s


def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    # 현재 시간으르 초로 변환
    m, s = int(pos.split(':')[0]), int(pos.split(':')[1])
    s += m * 60
    
    # 명령 순회
    for cmd in commands:        
        
        # 명령 수행 전 오프닝 구간인지 확인하고 맞으면 점프
        s = jump_opening(op_start, op_end, s)
        
        # 명령 수행
        if cmd == 'prev':
            s -= 10                 # 10초 이전으로 가고
            s = max(0, s)           # 음수면 0초로 초기화
        elif cmd == 'next':
            video_sec = int(video_len.split(':')[0]) * 60 + int(video_len.split(':')[1])
            s += 10                 # 10초 다음으로 가고
            s = min(s, video_sec)   # video_len보다 크면 video_len으로 초기화
    
        # 명령 수행 결과 오프닝 구간인지 확인하고 맞으면 점프
        s = jump_opening(op_start, op_end, s)

    # 초를 "분:초"로 변환
    m, s = s // 60, s % 60
    answer_m = str(m) if len(str(m)) > 1 else "0" + str(m)
    answer_s = str(s) if len(str(s)) > 1 else "0" + str(s)
    answer = answer_m + ":" + answer_s
    
    return answer