#-------------------------------------------------------------------------------
# Name:        module1
# Purpose: From learn python the hard way ex. 16
#
# Author:      Munnu
#
# Created:     26/08/2013
# Copyright:   (c) Munnu 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from sys import argv

"""script = argv
filename = 'littleText.txt'
txt = open(filename)

print "Here is your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

text_again = open(file_again)

print text_again.read()"""

script = argv
filename = 'littleText.txt'


print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()