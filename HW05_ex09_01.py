#!/usr/bin/env python
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the 
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def big_words():
	fin = open('words.txt')
	for line in fin:
		if len(line) > 20:
			print line



##############################################################################
def main():
    pass # Call your functions here.
    print big_words()

if __name__ == '__main__':
    main()
