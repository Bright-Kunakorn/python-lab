def calculate_score():
    n = int(input('Total students: '))
    first = 0
    second = 0
    sum_ = 0
    print('Enter score: ')
    for i in range(n):
        score = int(input())
        if score > first :
            second = first
            first = score
        elif score > second and score != first:
            second = score
        sum_ += score
    print('---')
    print('Max score is: {:.2f}'.format(first))
    if second == 0:
        print('Runner up is: None')
    else:
        print('Runner up is: {:.2f}'.format(second))
    print('Average is: {:.2f}'.format(sum_/n))

def main():
    calculate_score()

if __name__ =="__main__":
    main()
