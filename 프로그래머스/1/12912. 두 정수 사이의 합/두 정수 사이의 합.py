def solution(a, b):
    n = a if a <= b else b
    answer = 0
    while n <= (b if a <= b else a):
        answer += n
        n += 1
    return answer