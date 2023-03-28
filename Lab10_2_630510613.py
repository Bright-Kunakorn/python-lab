#630510613
#คุณากร โทปุรินทร์
#section 3
#Lab10_2

def calculate_p2p_evolve_exp(p, c) :
    evo = 0 //
    count = 0
    while p > 0:
        evo  += (c+count+p)//12
        c = c  %  12
        p-=1
    ans = evo*500
    return ans
    

def main():
    print(calculate_p2p_evolve_exp(3, 12))
    print(calculate_p2p_evolve_exp(2, 12))
    print(calculate_p2p_evolve_exp(2, 22))
    
if __name__ == '__main__':
    main()