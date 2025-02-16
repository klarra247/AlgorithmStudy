def solution(cards1, cards2, goal):
    used1 = 0
    used2 = 0
    
    for word in goal:
        if used1 < len(cards1) and word == cards1[used1]:
            used1 += 1
        elif used2 < len(cards2) and word == cards2[used2]:
            used2+= 1
        else:
            return 'No'
        
    return 'Yes'