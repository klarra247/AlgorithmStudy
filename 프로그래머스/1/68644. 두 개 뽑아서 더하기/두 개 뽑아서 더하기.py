def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            sumval = numbers[i] + numbers[j]
            if sumval not in answer:
                answer.append(sumval)
    answer.sort()
    return answer