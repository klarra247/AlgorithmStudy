def find_nth_doomsday(n):
    doomsday = 666
    count = 0

    while True:
        if '666' in str(doomsday):
            count += 1
            if count == n:
                return doomsday
        doomsday += 1

# 입력 받기
n = int(input())

# N번째 영화의 제목에 들어간 수 출력
print(find_nth_doomsday(n))