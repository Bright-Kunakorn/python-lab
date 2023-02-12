#630510613
#คุณากร โทปุรินทร์
#section 3
#Lab10_3
def nondest_rotate_list(list_a, n):
    return -n % len(list_a)

def main():
    print(nondest_rotate_list([1,2,3,4], 1)) 
    print(nondest_rotate_list([1,2,3,4], 10))
    print(nondest_rotate_list([1,2,3,4], -1))
if __name__=='__main__':
    main()
