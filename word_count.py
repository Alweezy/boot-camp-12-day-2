def word_count(input_string):
	"""
		Counts the number of words in a string and its number of occurances

		:param input_string
    	:return my_dictionary:
	"""
	my_dictionary = {}
	my_string = input_string.split()
	for word in my_string:
		dictionary_keys = my_dictionary.keys()
		if word not in dictionary_keys:
			my_dictionary[word] = 1
		else:
			my_dictionary[word] += 1
	return my_dictionary

print word_count("check this out and me out ")