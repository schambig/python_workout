def get_volume(length=1, width=2, depth=3):
    return length * width * depth, width, 'Salo'

vol, len, text = get_volume(width=7)

print(vol)
print(len)
print(text)
