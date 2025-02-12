from collections import deque

def solution(s):
    q = deque()
    answer = 0
    
    for i in s:
        if not i.isalpha():
            q.append(i)
            
    for i in range(len(q)):
        q.append(q.popleft())
        
        if isParenthesis(list(q)):
            answer += 1
    
    return answer

def isParenthesis(s):
    q1 = deque(s[0])
    q2 = deque(s[1:])
    par = {
        '}' : '{',
        ']' : '[',
        ')' : '('
        }
    
    while q2:
        if q1:
            a = q1.pop()
            b = q2.popleft()

            if b not in par or par[b] != a:
                q1.append(a)
                q1.append(b)
        else:
            q1.append(q2.popleft())
            
    if q1:
        return False
    else:
        return True
        
            
        
        
        
        