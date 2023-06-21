file = open('./zenpy.txt')
# print(file.read()) #
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

for line in file:
  print(line)

file.close()

with open('./zenpy.txt') as file:
  for line in file:
    print(line)


'''
What does "with" do?

"with" secretly inserts two method calls:

with open(filename) as f:
# f.__enter__()
for one_line in f:
print(one_line)
# f.__exit__()

In the case of a file, f.__exit__() flushes and closes the file,
ensuring that all data is written (if appropriate) and that the file is closed.

Yes, the file will be closed anyway when the Python program exits.
But this guarantees that the file is closed at a known time.

Any object that defines __enter__ and __exit__ is known as a context manager.
Files are the most famous, but other objects (e.g., threading.Lock) also support them.
'''