def three_digits_to_word(n):
    ans = ""
    x = n
    list_1 = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    list_2 = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    if n==0:
        return "zero"
    if n>99:
        ans = ans+list_1[x//100]+" hundred" ##hundred digit
        if x%100 > 19:
            ans = ans+" "+list_2[(x%100)//10] ##add ten digit
            
            if x%10!=0:
                ans =ans+"-"+list_1[(x%100)%10]  ##add once digit
        else:
            ans = ans+" "+list_1[x%100] ##add 1-19
    else:
        if x > 19:
            ans = ans+list_2[x//10] ##add ten digit
            
            if x%10!=0:
                ans =ans+"-"+list_1[x%10]   ##add once digit
        else:
            ans = ans+list_1[x] ##add once digit 1-19
    return ans

def num_to_word(num):
    x = num
    ans = ""
    if num <= 999:
        return three_digits_to_word(num) 
    if x//pow(10,9)>0:
        ans =  three_digits_to_word(x//pow(10,9))+" billion"  ##add billion digit
        x = x%pow(10,9)
    if x//pow(10,6)>0:
        ans = ans+" "+three_digits_to_word(x//pow(10,6))+" million" ##add million digit
        x = x%pow(10,6)
    if x//pow(10,3)>0:
        ans = ans+" "+three_digits_to_word(x//pow(10,3))+" thousand" ##add thousand digit
        x = x%pow(10,3)
    if x<1000:
        ans+= " "+three_digits_to_word(x) ##add hundred digit
        
    if ans[0]==" ":
        ans = ans[1:] ##if ans has white space in fornt 
        
    if ans[-4::] == "zero":
        ans = ans[0:len(ans)-5] ##if ans has "zero" in back    
    return ans

def main():
    print(num_to_word(1123))

if __name__=="__main__":
    main()
