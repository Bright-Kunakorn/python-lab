# Initialize the size of the matrix and a counter for the values to be filled in
num = 5
n_list = [[0 for x in range(num)] for y in range(num)]
n = 1

# Initialize the indices of the first and last elements in the current layer of the spiral
low = 0
high = num-1

# Calculate the number of times the inner loops need to be executed
count = int((num+1)/2)

# Loop over the layers of the spiral
for i in range(count):
    # Fill in the elements of the current row
    for j in range(low, high+1):
        n_list[i][j] = n
        n += 1
    # Fill in the elements of the current column
    for j in range(low+1, high+1):
        n_list[j][high] = n
        n += 1
    # Fill in the elements of the current row in reverse
    for j in range(high-1, low-1, -1):
        n_list[high][j] = n
        n += 1
    # Fill in the elements of the current column in reverse
    for j in range(high-1, low, -1):
        n_list[j][low] = n
        n += 1
    # Move to the next layer of the spiral
    low += 1
    high += 1

# Print the matrix
for i in range(num):
    for j in range(num):
        print(n_list[i][j], end='\t')
    print()
