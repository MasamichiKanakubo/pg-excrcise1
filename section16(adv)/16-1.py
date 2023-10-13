#ans

"""
解法が思いつかないので後に回す
pushはとりあえずしておく
"""


def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift_amount) % 26) + ord('A'))
        else:
            decrypted_char = char
        plaintext += decrypted_char
    return plaintext

ciphertext = "qdq-gi.q-a ziatmxxitmdqibtqi-ustbi ri.qmoqrcxi.qbubu zir -ibtqi-qpqaai ripmymsqkir -ibtqi-qy dmxi ri.cnxuoi rruoumxakir - ibtqiqzmobyqzbkii-q.qmxi -imyqzpyqzbi rixmeaki -puzmzoqai -i-qscxmbu zaimzpir -i btq-iymbbq-a;iz -iatmxximzgi.q-a zinqiuzimzgiemgipuaouyuzmbqpimsmuzabir -ia. za -uzsiacotiimi.qbubu zj カギはpersonです。解読してください"
for shift in range(26):
    decrypted_text = caesar_decrypt(ciphertext, shift)
    print(f"Shift {shift}: {decrypted_text}")
