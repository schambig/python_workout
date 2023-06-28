with open('./text.txt', 'w+') as file: # See notes for: w, r, r+, a, a+
  for line in file:
    print(line)
  file.write('This is a new line\n')
  file.write('Another line\n')
  file.write('And more lines yay!\n')

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

# NOTES:
# r     Opens the file for reading only.
# r+	Opens the file for both reading and writing. If the file does not exist, a FileNotFoundError exception is raised.
# w	    Opens the file for writing only. Any existing data in the file will be overwritten.
# w+	Opens the file for both writing and reading. Any existing data in the file will be overwritten.
#       If the file does not exist, the file is created.
# a	    Opens the file for appending. Any new data that you write to the file will be appended to the end of the file.
# a+	Opens the file for both appending and reading.
#       If the file does not exist, the file is created.
#       Any new data that you write to the file will be appended to the end of the file. You can also read the existing data in the file.

# Python File Write
# https://www.w3schools.com/python/python_file_write.asp

