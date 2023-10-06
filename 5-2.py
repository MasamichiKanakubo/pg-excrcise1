#ans

lv1 = int(input('勇者のレベル：'))
lv2 = int(input('戦士のレベル：'))
lv3 = int(input('魔法使いのレベル：'))
lv4 = int(input('僧侶のレベル：'))

"""
#先に最適解を書いておく


list = [lv1,lv2,lv3,lv4]

print('パーティの中で最もレベルの高いメンバのレベルは'+str(max(list))+'です。')
"""

#if文を使ったおそらく想定している解法
if lv1 >= lv2 and lv1 >= lv3 and lv1 >= lv4:
    max = lv1
elif lv2 >= lv1 and lv2 >= lv3 and lv2 >= lv4:
    max = lv2
elif lv3 >= lv1 and lv3 >= lv2 and lv3 >= lv4:
    max = lv3
elif lv4 >= lv1 and lv4 >= lv2 and lv4 >= lv3:
    max = lv4

print('パーティの中で最もレベルの高いメンバのレベルは'+str(max)+'です。')
    
