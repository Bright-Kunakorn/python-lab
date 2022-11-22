n = 10
sep = ''
def square_frame(n,sep):
    if sep  ==  "":
        sep =  " "
    number = list(range(1 , (n*3) + (n-3)))
    number = list(map(lambda x,y = 2: '0'*(y - len(str(x))) + str(x) , number))
    head   = number[:n]
    base   = number[n+(n-2):-(n-2)]
    base   = base[::-1]
    left   = number[-1-(n-2)+1:]
    left   = left[::-1]
    right  = number[n:(2*n)-2]
    body   = list(zip(left,right))
    head   = sep.join(head)
    base   = sep.join(base)
    body   = body,sep[0]*(len(sep.join(head))-(len(head[0])*2))
    ans    = head+"\n"+body+"\n"+base
    print(ans)

def left_and_right(x,y):
    if not x:
        return ''
    else:
        print(y.join(x[0]))
        return left_and_right(x[1:],y)
square_frame(n, sep)