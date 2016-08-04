#exercise 15
# from the system prompt get the script and file name
from sys import argv

#unpack the argument vector
script, filename = argv

#assign a function to a variable
txt = open(filename)

print "-----------"

#print out the file using the function .read() without parameters
print "Here's your file %r:" % filename
print txt.read()

print "-----------"

#this section asks for a file input and then prints the file

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()

#this is my attempt to skip over assigning a the open function to a variable
#it worked. i think a variable is still good to cut down on typing and maybe
#forgetting a parameter, if one was assigned
print "-----------"

print open(filename).read()