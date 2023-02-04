#630510613
#คุณากร โทปุรินทร์
#section 3
#Lab10_1
# Define a function to check if two strings are anagrams of each other.
def  is_anagram(s1, s2):
    # Remove spaces and convert both strings to lowercase.
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    
    # Check if the sorted versions of the strings are equal.
    if word_sort(s1) == word_sort(s2):
        return True
    else:
        return False

# Define a function to sort the characters in a string in ascending order.
def word_sort(l):
    # If the list has a length of 1 or less, return the list as is.
    if len(l) <= 1:
        return l
    else:
        # Return the list sorted into three parts: all elements that are smaller than the first element,
        # the first element itself, and all elements that are larger than the first element.
        return word_sort([e for e in l[1:] if e <= l[0]]) + [l[0]] +\
            word_sort([e for e in l[1:] if e > l[0]])

def main():
    # Call the is_anagram function and print the result.
    print(is_anagram('I am Lord Voldemort','Tom Marvolo Riddle'))
    
if __name__ == '__main__':
    main()
