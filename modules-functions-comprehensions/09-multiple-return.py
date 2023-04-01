def get_volume(length=1, width=2, depth=3):
    return length * width * depth, width, 'Salo'

# res = get_volume(width=7) # This will return a tuple
vol, width, text = get_volume(width=7)

# print(res) # (21, 7, 'Salo')
print(vol) # 21
print(width) # 7
print(text) # Salo
