def solution(strings, n):
    newstrings = []
    answer = []
    for string in strings:
        newstrings.append(string[n] + string)
    newstrings = sorted(newstrings)
    
    for newstring in newstrings:
        print(newstring[1:])
        answer.append(newstring[1:])
        
    return answer