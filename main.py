from stats import get_num_words, char_count, show_order_char_count
import sys

def get_book_text_info(filepath):
    with open(filepath) as f:
        file_contents = f.read()                                #store txt data in var
        num_of_words = get_num_words(file_contents)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_of_words} words in total")
        print("--------- Character Count -------")
        char_dict = char_count(file_contents)                   #returns dict w all chars & corrs count
        ordered_list = show_order_char_count(char_dict)         #returns order list of only alpha char & count
        for item in ordered_list:                               #for each item in list, 
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
        

def main():
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: python3 main.py <relative_path_to_book>")
        sys.exit(1)
    
    elif len(sys.argv) > 1:                   #first arg is the script name
        filepath = sys.argv[1]
        get_book_text_info(filepath)
 

main()
