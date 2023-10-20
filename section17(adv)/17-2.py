#ans

palindrome = input('なんでも回文にします。入力してください:')
list = list(palindrome)
print(list)

for i in range(len(list) // 2):
    if list[i] != list[-(i + 1)]:
        print('回文ではありません')
        break
    else:
        if i == len(list) // 2 - 1:
            pass