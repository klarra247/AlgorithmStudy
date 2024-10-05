def solution(seoul):
    for index, person in enumerate(seoul):
        if person == "Kim":
            return "김서방은 " + str(index) + "에 있다"
