def solution(s):
    changes = {
        'zero': '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    temp = ''
    answer = ''
    for char in s:
        if char.isalpha():
            temp += char
            if temp in changes:
                answer += changes[temp]
                temp = ''
        else:
            answer += char
                
    return int(answer)