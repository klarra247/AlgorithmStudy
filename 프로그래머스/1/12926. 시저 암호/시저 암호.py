def solution(s, n):
    answer = ''
    n = n % 26
    for char in s:
        if char.isalpha():
            if char.islower():
                if chr(ord(char) + n).isalpha() and chr(ord(char) + n).islower() :
                    answer += chr(ord(char) + n)
                else:
                    answer += chr(ord(char) + n - 26)
            else:
                if chr(ord(char) + n).isalpha() and chr(ord(char) + n).isupper() :
                    answer += chr(ord(char) + n)
                else:
                    answer += chr(ord(char) + n - 26)
        else:
            answer += char
                
    return answer