#ans

decision = True
while decision:
    response = int(input('王様「わしの頼みを聞いてくれるかな？」:\n[0]はい/[1]いいえ:'))  
    if response == 0:
        decision = False

print('おお！よくぞ申した！それでこそ真の勇者よ！')