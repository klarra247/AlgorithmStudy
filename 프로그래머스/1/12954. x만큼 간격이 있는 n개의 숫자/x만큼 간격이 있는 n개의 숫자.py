def solution(x, n):
    a = x
    answer = []
    for i in range(n):
        answer.append(a)
        a += x
    return answer