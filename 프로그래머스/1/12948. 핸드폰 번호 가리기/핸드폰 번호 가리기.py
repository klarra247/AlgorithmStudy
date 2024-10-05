def solution(phone_number):
    phone_number_list = list(str(phone_number))[::-1]
    
    return (len(phone_number_list) - 4) * "*" + ''.join(phone_number_list[:4][::-1])
    