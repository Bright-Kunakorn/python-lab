def matrix_mult(m1, m2):
    # Initialize an empty list to store the result
    result = []

    # Iterate over the rows in m1
    for i in range(len(m1)):
        # Initialize an empty list to store the result row
        row = []
        # Iterate over the columns in m2
        for j in range(len(m2[0])):
            # Initialize the product to 0
            product = 0
            # Iterate over the elements in the row of m1 and the column of m2
            for v in range(len(m1[i])):
                # Multiply the corresponding elements and add the result to the product
                product += m1[i][v] * m2[v][j]
            # Append the product to the result row
            row.append(product)
        # Append the result row to the result
        result.append(row)
    # Return the result
    return result
