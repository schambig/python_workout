def get_volume(length=1, width=2, depth=3):
    return length * width * depth, width, 'Salo'

res = get_volume(width=7)
vol, len, text = get_volume(width=7)

print(res)
print(vol)
print(len)
print(text)
