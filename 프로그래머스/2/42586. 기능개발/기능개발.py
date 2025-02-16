def solution(progresses, speeds):
    answer = []
    stack = []

    for progress, speed in zip(progresses, speeds):
        if (100 - progress) % speed == 0:
            stack.append((100 - progress) // speed)
        else:
            stack.append((100 - progress) // speed + 1)
        # stack.append(100 - progress + speed)
        
    num = 1
    day = stack[0]
    
    for i in range(1, len(stack)):
        if stack[i] <= day:
            num += 1
        else:
            answer.append(num)
            num = 1
            day = stack[i]
            
    answer.append(num)
    
    return answer