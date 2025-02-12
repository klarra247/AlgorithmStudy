from collections import deque

def solution(s):
    q1 = deque(s[0])
    q2 = deque(s[1:])
    
    while q2:
        if q1:
            a = q1.pop()
            b = q2.popleft()

            if a != b:
                q1.append(a)
                q1.append(b)
        else:
            q1.append(q2.popleft())
                
    if q1:
        return 0
    else:
        return 1