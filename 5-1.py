#ans

print('勇者の攻撃力とスライムの防御力を入力してください。')
attack = int(input('勇者の攻撃力：'))
defense = int(input('スライムの防御力：'))
damage = attack - defense

if damage <= 0:
    print('スライムはダメージを受け付けない。')
else:
    print('勇者はスライムに'+str(damage)+'のダメージを与えた！')