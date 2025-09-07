from stats import get_word_count, get_letter_count, get_list
import sys

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	location = sys.argv[1]
	string = get_book_text(location)
	num_words = get_word_count(string)
	letter_dict = get_letter_count(string)
	sorted_dict = get_list(letter_dict)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {location}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in sorted_dict:
		if not item["char"].isalpha():
			continue
		print(f"{item['char']}: {item['num']}")
	print("============= END ===============")




	
def get_book_text(file):
	with open(file) as f:
		return f.read()

def sort_on(letters):
	return letters["count"]
	
if __name__ == "__main__":
    main()	 
