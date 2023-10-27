#ans

"""
N: 10G
O: 15G
*をNかOに置き換えて置き換えた分だけ請求する
"""

palindrome = input('なんでも回文にします。入力してください:')
n_count = 0
o_count = 0
for idx, string in enumerate(palindrome):
    if string == palindrome[-idx-1] == '*':
        x = palindrome.replace(string, 'N')
        n_count += 1
    elif string == '*' and palindrome[-idx-1] == 'N':
        x = palindrome.replace(string, 'N')
        n_count += 1
    elif string == '*' and palindrome[-idx-1] == 'O':
        x = palindrome.replace(string, 'O')
        o_count += 1
    
print(x)
print(f'n:{n_count*10}G, o:{o_count*15}Gで合計{n_count*10+o_count*15}です')