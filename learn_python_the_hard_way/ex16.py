from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit Ctrl+C (^C)."
print "If you want that, hit ENTER."

raw_input("? ")

print "opening the file..."
target = open(filename,"w")

print "Truncating the file. 2333333"
target.truncate()

print "Now we are going to type new lines into the file."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "We are going to write these lines to the file..."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

