def calculate_score():
    # Get the total number of students from user input
    n = int(input('Total students: '))

    # Initialize variables to store the maximum and second maximum scores
    first = 0
    second = 0

    # Initialize a variable to store the sum of all scores
    sum_ = 0

    # Prompt the user to enter the scores
    print('Enter score: ')
    for i in range(n):
        score = int(input())

        # Update the maximum and second maximum scores if necessary
        if score > first:
            second = first
            first = score
        elif score > second and score != first:
            second = score

        # Add the score to the sum
        sum_ += score

    # Print the maximum, second maximum, and average scores
    print('---')
    print('Max score is: {:.2f}'.format(first))
    if second == 0:
        print('Runner up is: None')
    else:
        print('Runner up is: {:.2f}'.format(second))
    print('Average is: {:.2f}'.format(sum_/n))

def main():
    # Call the calculate_score function
    calculate_score()

# Check if the script is being run directly and not imported as a module
if __name__ =="__main__":
    main()
