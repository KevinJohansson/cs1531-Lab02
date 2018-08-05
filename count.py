'''
 Exercise 3:
 Given a paragraph of text, 
 1. count the number of times each character occurs in the text, 
   and print out each character and its count (in any order).
 2. do it now in a case-insensitive manner for the alphabets
 3. extension: print in the descending order of the count
'''


def count_char(text):
    # add your code here
	dictionary = {}
	for i in range(len(text)):
		dictionary[text[i]] = 0
	for i in range(len(text)):
		dictionary[text[i]] += 1
	
	for i in dictionary:
		print(i + " " + str(dictionary[i]))


def count_char_insensitive(text):
    # add your code here
	dictionary = {}
	for i in range(len(text)):
		val = text[i]
		val = val.lower()
		dictionary[val] = 0
	for i in range(len(text)):
		val = text[i]
		val = val.lower()
		dictionary[val] += 1
	
	for i in dictionary:
		print(i + " " + str(dictionary[i]))

# bonus task:
#def count_char_ordered(text):
    #pass
    # add your code here 

text1 = "I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn't really happy" # Robert Bolano
text2 = 'HellO, WorLd!'

# testing exercise 2
count_char(text2)
count_char_insensitive(text2)
#count_char_ordered(text2)

