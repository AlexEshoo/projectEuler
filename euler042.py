from eulerTools import triangleNumber, is_triangular

with open("resources/p042_words.txt", 'r') as f:
    words = f.read().strip().split(',')
    words = [w.strip('"') for w in words]


def is_triangle_word(word):
    ASCII_OFFSET = 64
    n = 0
    for c in word:
        n += ord(c) - ASCII_OFFSET

    if is_triangular(n):
        return True

    return False

count = 0
for w in words:
    if is_triangle_word(w):
        count += 1

print("Answer:", count)
