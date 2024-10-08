def solution(s):
    answer = ''
    words = s.split(' ')
    for word in words:
        answer += ' '   
        for i in range(len(word)):
            if i % 2 == 0:
                if word[i].islower():
                    answer += word[i].upper()
                else: 
                    answer += word[i]
            else:
                if word[i].isupper():
                    answer += word[i].lower()
                else: 
                    answer += word[i]
                
            
    return answer[1:]