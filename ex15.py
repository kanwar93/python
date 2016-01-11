# imports the arugmetn var from sys which is a package 
from sys import argv 
# script and filename are the argv
script, filename = argv
# opens the file
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()