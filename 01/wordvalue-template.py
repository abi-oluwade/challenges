from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    # Sets variable to dictionary.txt
    dict_list = open(DICTIONARY)
    # Sets a variable to an empty array to append list
    x = []

    # Simple for-loop logic, strip used to remove spaces at start and end of strings, then set variable
    # to split the newly stripped line from txt file, finally append stripped and split line to empty an empty list
    for line in dict_list:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        x.append(line_list)
    dict_list.close()
    print(x)
    pass

def calc_word_value():
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    pass

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
    pass # run unittests to validate

print(load_words())