def remove_row_col(list_a, row, col):
    # Create a copy of list_a
    ans = list_a[:]
    
    # Iterate over the rows in ans
    for i in range(len(ans)):
        # Remove the specified column from the current row
        ans[i].pop(col)
    
    # Remove the specified row
    ans.pop(row)
    
    # Return the modified list
    return ans
