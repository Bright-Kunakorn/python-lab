def remove_row_col(list_a, row, col):
    ans = list_a
    for i in range(len(ans)):
        del ans[i][col]
    del ans[row]
    return ans

def main():
    print(remove_row_col([[2, 3, 4], [8, 7, 6], [0, 1, 2]], 1, 2))
    print(remove_row_col([[2, 3, 4, 5], [8, 7, 6, 5], [0, 1, 2, 3]], 1, -3))
if __name__=="__main__":
    main()
