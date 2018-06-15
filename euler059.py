def keys():
    # 97-122 ascii are lowercase letters
    for i in range(97,123):
        for j in range(97,123):
            for k in range(97,123):
                key = [i, j, k]
                yield key

def get_text(decrypted):
    chars = [chr(i) for i in decrypted]
    text = ''.join(chars)
    return text

with open("resources/p059_cipher.txt") as f:
    txt = f.read()

encrypted = [int(i) for i in txt.split(',')]
length, rem = divmod(len(encrypted), 3)

for key in keys():
    cipher = key * length
    cipher.extend(key[:rem])
    decrypted = [i ^ cipher[j] for j,i in enumerate(encrypted)]

    flag = 1
    for n in decrypted:
        if n not in range(32,127):
            flag = 0
            break

    if not 'Gospel' in get_text(decrypted):  # First identified existence of this word by filtering on word 'the'
        flag = 0

    if flag:
        print(get_text(decrypted))
        print(sum(decrypted))