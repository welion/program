def break_words(stuff):
	words = stuff.split(' ')
	return words

def sort_words(stuff):
	return sorted(stuff)

def print_first_word(stuff):
	word = stuff.pop(0)
	print word

def print_last_word(stuff):
	word = stuff.pop(-1)
	print word

def sort_sentence(sentence):
	words = break_words(sentence)
	return soret_words(words)

def print_first_and_last_word(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted_words(sentence):
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

