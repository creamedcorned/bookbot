def get_word_count(string):
	return len(string.split())

def get_letter_count(string):
	letter_count = {}
	for letter in string.lower():
		if letter not in letter_count:
			letter_count[letter] = 1
		else:
			letter_count[letter] += 1
	return letter_count

def sort_on(dict):
    return dict["num"]

def get_list(dict):
	list = []
	for char in dict:
		list.append({"char": char, "num": dict[char]})
	list.sort(reverse=True, key=sort_on)
	return list