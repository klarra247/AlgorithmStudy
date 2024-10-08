def solution(price, money, count):
    total = count * (2 * price + price * (count - 1) ) / 2
    
    if total <= money:
        return 0
    else:
        return total - money
