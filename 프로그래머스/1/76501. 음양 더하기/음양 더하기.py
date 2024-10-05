def solution(absolutes, signs):
    numbers = []
    
    for i in range(len(signs)):
        numbers.append(("+" if signs[i] else "-") + str(absolutes[i]))
    
    return sum(list(map(int, numbers)))
    
