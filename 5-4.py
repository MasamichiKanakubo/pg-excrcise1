#ans

print('スライムがあらわれた！')
print('スライムはなかまになりたそうにじっとこっちを見ている。')

answer = str(input('[0]仲間にする\n[1]戦う\n[2]逃げる\n選択：'))
if answer == str(0):
    print('スライムはなかまになった！')
elif answer == str(1):
    print('勇者はスライムを倒した！')
else:
    print('勇者は逃げた！')