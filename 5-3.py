#ans

print('勇者の攻撃力とゴブリンの守備力, HPを入力してください。')

attack = int(input('勇者の攻撃力：'))
defense = int(input('ゴブリンの守備力：'))
hp = int(input('ゴブリンのHP：'))

print('勇者の攻撃！')

damage = attack - defense 
if damage <= 0:
    print('ゴブリンはダメージを受け付けない。')
else:
    print('ゴブリンに'+str(damage)+'のダメージを与えた！')
    
hp -= damage
if hp <= 0:
    print('ゴブリンを倒した！')
else:
    print('ゴブリンのHP',hp)

