#ans

medicinal_herb = 10
antidote = 25
panacea = 100

num_medi = int(input('道具屋「薬草(10G)をいくつかいますか？」：'))
num_anti = int(input('毒消し(25G)をいくつかいますか？：'))
num_pana = int(input('万能薬(100G)をいくつかいますか？：'))

price = medicinal_herb * num_medi + antidote * num_anti + panacea * num_pana

print('薬草'+str(num_medi)+'個、'+'毒消し'+str(num_anti)+'個、'+'万能薬'+str(num_pana)+'個ですね。合計で'+str(price)+'Gです。')

"""
input関数を使ってユーザーに数値を入力させる
二行に分けずに一行で入力と型変換は行う
合計金額などの演算などはロジックとして一度公式的に定義して変数に入れておく
変数名は一発でそれについてわかるように命名する
"""