def solution(s):
    answer = []
    for char in s:
        answer.append(ord(char))
        
    answer.sort(reverse = True)
    
    return ''.join(list(map(chr, answer)))
