def dest_rotate_list(list_a, n):
    b = list_a[-n % len(list_a):] + list_a[:-n % len(list_a)]
    list_a[:] = []
    list_a += b

def main():
    list_a = [1,2,3,4]
    dest_rotate_list(list_a, 1)
    print(list_a)
    
if __name__=='__main__':
    main()
