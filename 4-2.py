yakuso = 10
dokukeshi = 25
bannno_yaku = 100

amount1 = int(input('道具屋「薬草(10G)をいくつかいますか？」：'))
amount2 = int(input('毒消し(25G)をいくつかいますか？：'))
amount3 = int(input('万能薬(100G)をいくつかいますか？：'))
price = yakuso * amount1 + dokukeshi * amount2 + bannno_yaku * amount3
print('薬草'+str(amount1)+'個、'+'毒消し'+str(amount2)+'個、'+'万能薬'+str(amount3)+'個ですね。合計で'+str(price)+'Gです。')