def reverse_Check(word):
	if word == word[::-1]:
		print 'same'
	else:
		print 'different'

word = raw_input("Iuput your string: ")
reverse_Check(word)
