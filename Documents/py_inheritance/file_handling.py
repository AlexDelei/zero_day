"""
Reading and writing files

open() returns a file object and ismost commonly used with two positional arguments and one keyword argument:
  open(filename, mode, encoding=None)


Example:
>>> f = open('workfile', 'w', encoding="utf-8")

explanation:
The first argument is a string containing the filename.
The second argument is another string containing a few characters describing the way in which the file will be used.
 'r' - for reading only
 'w' - writing only
 'a' - opens the file for appending; any data written to the file is automatically added to the end.
 
 'b' -  Appending a 'b' to the mode opens the file in binary mode.


NB: It is good practice to use the with keyword when dealing with file objects
    -> The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point.

Example
>>> with open('workfile', encoding="utf-8") as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True


"""

############

"""
Methods of file objects

Assumption:
A file object called f has already been created


To read a file's contents, call f.read(size)
  -> which reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode).

If the end of the file has been reached, f.read() will return an empty string ('')

Example:
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''

f.readline() reads a single line from the file;
a newline character (\n) is left at the end of the string

For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:
>>> for line in f:
...     print(line, end='')


####

f.write(string) writes the contents of string to the file, returning the number of characters written.

Example:
>>> f.write('This is a test\n')
15

NB: Other types of objects need to be converted - either to a string (in text mode) or a bytes object (in binary mode) - before writing them:
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18

####

To change the file object's position, use f.seek(offset, whence)

Example:
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'


"""

"""
Saving structured data with JSON

Strings can easily be written to and read from a file. 
Numbers take a bit more effort, since the read() method only returns strings,
which will have to be passed to a function like int(), which takes a string like '123' and returns its numeric value 123.
When you want to save more complex data types like nested lists and dictionaries, parsing and serializing by hand becomes complicated.

Rather than having users constantly writing and debugging code to save complicated data types to files, 
Python allows you to use the popular data interchange format called JSON (JavaScript Object Notation). 
The standard module called json can take Python data hierarchies, and convert them to string representations; 
this process is called serializing. Reconstructing the data from the string representation is called deserializing.
Between serializing and deserializing, the string representing the object may have been stored in a file or data,
or sent over a network connection to some distant machine.

Example:

>>> import json
>>> x = [1, 'simple', 'list'] 
>>> json.dumps(x) # serializing 
'[1, "simple", "list"]' # object x string representation

dump() - simply serializes the object to a text file

Example:
>>> json.dump(x, f)


"""