# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 11:12:35 2015

@authors: 
Shubham 
Suzanne
"""

# Program to convert text into hAck3r using regular expressions and substitution.

################################## Imports ####################################
import re

#	reads the authors information from a text file "authors.txt"
file = open('authors.txt')
readRaw = file.read()

# lowercases the text
readRaw = readRaw.lower()

################################## Methods ####################################
def convert_to_hacker(text):
	"""converts a text to hacker"""
	new_text = []

	#initial pass subsitutes 8 for ate.
	pattern = re.compile(r'ate')
	text = pattern.sub('8', text) 

	# regex that searches through the text to find instances of the letters 
      # to be converted.
	pattern = re.compile(r'[eiols]|\.')


	# converts all the letters
	for w in text:
		if re.search(pattern, w):
			if w == 'e':
				w = '3'
			elif w == 'i':
				w = '1'
			elif w == 'o':
				w = '0'
			elif w == 's':
				w = '5'
			elif w == 'l':
				w = '|'
			elif w == '.':
				w = '5w33t!'
		new_text.extend(w)
	new_text = ''.join(new_text)

	# regex searching for word initial s.
	pattern = re.compile(r'\b5')
	new_text = pattern.sub('$', new_text)

	return new_text

text = convert_to_hacker(readRaw)
print(text)

################################ End of File ##################################