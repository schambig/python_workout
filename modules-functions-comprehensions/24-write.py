with open('./text.txt', 'w+') as file: # See notes for: w, r, r+, a, a+
  for line in file:
    print(line)
  file.write('This is a new line\n')
  file.write('Another line\n')
  file.write('And more lines yay!\n')