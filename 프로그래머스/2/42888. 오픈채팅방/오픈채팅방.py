def solution(record):
    nickname = {}
    order = []
    answer = []
    
    for i in record:
        i = i.split()
        if i[0] == "Enter":
            order.append([i[0], i[1]])
            nickname[i[1]] = i[2]
        elif i[0] == "Leave":
            order.append([i[0], i[1]])
        else:
            nickname[i[1]] = i[2]

    for result in order:
        if result[0] == "Enter":
            answer.append(f"{nickname[result[1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{nickname[result[1]]}님이 나갔습니다.")

    return answer