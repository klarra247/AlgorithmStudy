def solution(s):
    answer = []
    number = 0
    s = s[::-1]
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                number = j - i
                break
        if number == 0:
            answer.append(-1)
        else: 
            answer.append(number)
        number = 0

    return [-1] + answer[::-1]