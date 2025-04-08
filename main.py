from stats import word_count, char_count, char_sort
import sys

def get_books_text():
    
    #Open the file as f, then return it to be saved as file_contents
    with open(sys.argv[1]) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")

    print(f"Analysing book found at {sys.argv[1]}")

    #Grabbing the content of the book and assigning the value
    file_contents = get_books_text()

    print("----------- Word Count ----------")

    #Grab the word count and present it nicely
    word_count_result = word_count(file_contents)
    
    print(f"Found {word_count_result} total words")

    print("--------- Character Count -------")
    
    #Grab the character count and sort the results
    char_count_result = char_count(file_contents)

    #Sort the character count by value, decending
    char_sorted_result = char_sort(char_count_result)
    
    #In the sorted result, only print the key/ val if the key is alphanumeric (remove spaces and \n)
    for char, count in char_sorted_result:
        if char.isalpha():
            print(f"{char}: {count}")    

    print("============= END ===============")

main()