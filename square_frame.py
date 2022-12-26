# Initialize the size of the frame and the separator
n = 10
sep = ''

def square_frame(n, sep):
    # Set the default separator to a single space if none is provided
    if sep == "":
        sep = " "

    # Generate a list of integers from 1 to (n*3) + (n-3) and convert them to strings with leading zeros
    number = list(range(1, (n*3) + (n-3)))
    number = list(map(lambda x, y=2: '0'*(y - len(str(x))) + str(x), number))

    # Split the list into four parts: head, base, left, and right
    head = number[:n]
    base = number[n+(n-2):-(n-2)]
    base = base[::-1]
    left = number[-1-(n-2)+1:]
    left = left[::-1]
    right = number[n:(2*n)-2]

    # Zip the left and right parts together and join them using the separator
    body = list(zip(left, right))
    body = body, sep[0]*(len(sep.join(head))-(len(head[0])*2))

    # Join the head and base parts using the separator
    head = sep.join(head)
    base = sep.join(base)

    # Concatenate the head, body, and base parts to form the final output
    ans = head+"\n"+body+"\n"+base

    # Print the output
    print(ans)

# Helper function to recursively print the elements of left and right with y as a separator
def left_and_right(x, y):
    if not x:
        return ''
    else:
        print(y.join(x[0]))
        return left_and_right(x[1:], y)

# Call the square_frame function with the desired size and separator
square_frame(n, sep)
