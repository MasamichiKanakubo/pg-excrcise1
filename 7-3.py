#ans

print('勇者の攻撃力とゴーレムのHP、守備力を入力してください。')

offense = int(input('勇者の攻撃力:'))
hp = int(input('ゴーレムのHP:'))
defense = int(input('ゴーレムの防御力:'))

decision = True
while decision:
    option = int(input('[0]たたかう/[1]にげる:'))
    if option == 1:
        print('勇者はにげだした！')
        decision = False
        continue
    
    damage = offense - defense
    if damage > 0:
        print(f'ゴーレムに{damage}のダメージを与えた！')
    else:
        print('ゴーレムはダメージをうけていない！')
        continue
    
    hp -= damage
    if hp <= 0:
        hp = 0
        print('ゴーレムをたおした！')
        decision = False
    else:
        print(f'ゴーレムのHP:{hp}')
    

