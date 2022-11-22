#630510613
#คุณากร โทปุรินทร์
#section 3
#Lab10_1

def  is_anagram(s1, s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    if word_sort(s1) == word_sort(s2):
        return True
    else:
        return False

def word_sort(l):
    if len(l) <= 1:
        return l
    else:
        return word_sort([e for e in l[1:] if e <= l[0]]) + [l[0]] +\
            word_sort([e for e in l[1:] if e > l[0]])

def main():
    print(is_anagram('I am Lord Voldemort','Tom Marvolo Riddle'))
    
if __name__ == '__main__':
    main()
