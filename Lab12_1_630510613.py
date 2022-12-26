from datetime import date

# This function sorts a list of strings that represent dates in the format "DD/MM/YYYY"
# and returns a list of strings in the same format but sorted in ascending order.
def sort_date(list_x):
    d1 = []
    d2 = []
    # For each string in the input list, convert it to a date object using del1 and
    # append it to d1
    for i in list_x:
        date = str(del1(i))
        d1.append(date)
        
    # Sort d1 using a bubble sort algorithm
    list_x = bubbleSort(d1)
    
    # For each date in list_x, convert it back to a string using del2 and append
    # it to d2
    for i in list_x:        
        date = str(del2(i))
        d2.append(date)
    # Assign d2 to list_x and return it
    list_x = d2
    return list_x
    
# This function converts a string in the format "DD/MM/YYYY" to a date object
def del1(x):
    # Replace all "/" characters with " "
    x = x.replace("/"," ")
    # Split the string on " " characters
    x = x.split()
    # Create a date object using the year, month, and day components of x
    y = date(int(x[2]),int(x[1]),int(x[0]))
    return y

# This function converts a date object to a string in the format "DD-MM-YYYY"
def del2(x):
    # Replace all "-" characters with " "
    x = x.replace("-"," ")
    # Split the string on " " characters
    x = x.split()
    # Concatenate the year, month, and day components of x with "/" characters in between
    y = str(x[2])+"/"+ str(x[1])+"/"+str(x[0])
    return y

# This function sorts a list using a bubble sort algorithm
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():    
    print(sort_date(["11/1/2100","5/12/1999","19/1/2003","11/9/2001"]))

if __name__=="__main__":
    main()
