def solution(friends, gifts):
    # 두 사람이 선물을 주고받은 기록이 있다면, 
    # 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.
    
    # 두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면, 
    # 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받습니다.

    # 선물 지수는 이번 달까지 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값입니다.
    # 만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않습니다.

    # answer = 선물을 가장 많이 받을 친구가 받을 선물의 수

    # friends = 친구들 이름 배열 (중복 x)
    # gifts = ["A B",...] A: 준사람, B: 받은사람
    gift_dict = {friend: {other_friend: 0 for other_friend in friends} for friend in friends}
    gift_list = {friend: 0 for friend in friends}
    
    next_gift = {friend: 0 for friend in friends}
    
    for gift in gifts:
        a, b = gift.split(' ')
        gift_dict[a][b] += 1
        
        gift_list[a] += 1
        gift_list[b] -= 1
    
    for i in range(len(friends) - 1):
        for b in friends[i + 1:]:
            a = friends[i]
                
            if gift_dict[a][b] > gift_dict[b][a]:
                next_gift[a] += 1
            elif gift_dict[a][b] < gift_dict[b][a]:
                next_gift[b] += 1
            else:
                if gift_list[a] > gift_list[b]:
                    next_gift[a] += 1
                elif gift_list[a] < gift_list[b]:
                    next_gift[b] += 1
                

    return max(next_gift.values())