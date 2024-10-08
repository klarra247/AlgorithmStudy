def solution(n):
    answer = 0
    temp = []
    while n > 0:
        temp.append(n % 3)
        n = n // 3

    for i in range(len(temp)):
        answer += temp.pop() * 3 ** i
    return answer