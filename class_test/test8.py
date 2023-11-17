hp = 100

while hp > 0:
    answer = int(input("[0]たたかう/[1]にげる: "))
    if answer == 0:
        hp -= 5
        print(f'ゴーレムのHP: {hp}')
    elif answer == 1:
        break