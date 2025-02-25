from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        order_comb = {}
        
        for order in orders:
            order = ''.join(sorted(order))
            
            for comb in combinations(order, c):
                menu = ''.join(comb)
                if menu in order_comb:
                    order_comb[menu] += 1
                else:
                    order_comb[menu] = 1
        
        if order_comb:
            max_menu = max(order_comb.values())
            
            if max_menu >= 2:
                for menu, freq in order_comb.items():
                    if freq == max_menu:
                        answer.append(menu)
    
    return sorted(answer)