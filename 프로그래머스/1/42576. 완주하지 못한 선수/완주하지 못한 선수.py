def solution(participant, completion):
    di = dict()
    for i in participant:
        if i in di:
            di[i] += 1
        else:
            di[i] = 1
    for j in completion:
        di[j] -= 1
        if di[j] == 0:
            del(di[j])
    
    return list(di.keys())[0]