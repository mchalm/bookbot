def word_count(file_contents):

    #Find the word count of the file (split() is used to split each individual word), then print that value
    word_count = len(file_contents.split())
    return word_count

def char_count(file_contents):

    #Find the character count in the entire book

    #Defining the dictionary
    char_dict = {}

    #Iterate each character in the file
    for characters in file_contents:
        
        #Make each character lowercase to remove duplicates (M and m should be the same)
        lower_char = characters.lower()

        #If the character is not in the dictionary, add it
        if lower_char not in char_dict:
            char_dict[lower_char] = 0
        
        #Count the character and add update the dictionary
        char_dict[lower_char] += 1

    return char_dict


def char_sort(char_count_result):
    
    #Sort the character count result in decending order (reverse=True) by using sorted(). key=lamba is how the list is sorted by the value.
    sorted_char = sorted(char_count_result.items(), key=lambda item:item[1], reverse=True)

    #Return the value            
    return sorted_char