from sys import argv

script, filename = argv 

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Gooodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
line4 = raw_input("line 4: ")

print "I'm going to write these to the file."

#when you have repetition like this 

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
#target.write(line4)
#target.write("\n")

#you can rewite it like that to make a loop

data = (line1, "\n", line2, "\n", line3, "\n", line4, "\n")
for datum in data:
	target.write(datum)


print "And finally, we close it."
target.close()