def solution(array, commands):
    answer = []
    newarray = []
    for command in commands:
        newarray = array[command[0] - 1 : command[1]]
        newarray.sort()
        answer.append(newarray[command[2] - 1])
        newarray = []
        print(answer)
    return answer