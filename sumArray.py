def sumEven(x):
    sum_even = 0
    for i in range(len(x)):
        if not x[i].isdigit():
            if x[i] == ">":
                if i+1 < len(x):
                    x[i] = x[i+1]
            elif x[i] == "<":
                if i-1 >= 0:
                    x[i] = x[i-1]
        if not x[i].isdigit():
            if x[i] == ">":
                if i+2 < len(x):
                    x[i] = x[i+2]
            elif x[i] == "<":
                if i-2 >= 0:
                    x[i] = x[i-2]
        if x[i].isdigit() and int(x[i]) % 2 == 0:
            sum_even += int(x[i])

    return sum_even

def sumOdd(x):
    sum_odd = 0
    for i in range(len(x)):
        if not x[i].isdigit():
            if x[i] == ">":
                if i+1 < len(x):
                    x[i] = x[i+1]
            elif x[i] == "<":
                if i-1 >= 0:
                    x[i] = x[i-1]
        if not x[i].isdigit():
            if x[i] == ">":
                if i+2 < len(x):
                    x[i] = x[i+2]
            elif x[i] == "<":
                if i-2 >= 0:
                    x[i] = x[i-2]
        if x[i].isdigit() and int(x[i]) % 2 != 0:
            sum_odd += int(x[i])

    return sum_odd

x2 = ["1", "2", "<", "<", "<", "<", "6", ">", ">", "7"]
print(sumEven(x2))
print(sumOdd(x2))
