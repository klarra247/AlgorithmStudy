from collections import deque

def solution(want, number, discount):
    want_dict = {}
    answer = 0
    a = 10
    ten_days = deque(discount[:a])
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    original_want_dict = want_dict.copy()
    
    for i in range(len(discount) - 9):
        want_dict = original_want_dict.copy()
        
        for j in range(i, i + 10):
            if discount[j] in want_dict:
                want_dict[discount[j]] -= 1
        
        if all(num <= 0 for num in want_dict.values()):
            answer += 1
            
    return answer