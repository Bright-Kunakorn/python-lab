from datetime import date
def sort_date(list_x):
    d1 = []
    d2 = []
    for i in list_x:
        date = str(del1(i))
        d1.append(date)
        
    list_x = bubbleSort(d1)
    
    for i in list_x:        
        date = str(del2(i))
        d2.append(date)
    list_x = d2
    return list_x
    
def del2(x):
    x = x.replace("-"," ")
    x = x.split()
    y = str(x[2])+"/"+ str(x[1])+"/"+str(x[0])
    return y

def del1(x):
    x = x.replace("/"," ")
    x = x.split()
    y = date(int(x[2]),int(x[1]),int(x[0]))
    return y

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
