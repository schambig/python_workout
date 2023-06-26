file = open('./zenpy.txt')
# print(file.read()) # The read() method reads (prints) the whole content
# print(file.readline()) # This will read line by line
# print(file.readline()) # "
# print(file.readline()) # "
# print(file.readline()) # "

# This will also read (print) the whole file, line by line
for line in file:
  print(line)

file.close() # The close() method closes the file, freeing space memory

# This will also read (print) the file content and also close it, so no need to use 'file.close()' as in line 12
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

# Python File Open
# https://www.w3schools.com/python/python_file_handling.asp