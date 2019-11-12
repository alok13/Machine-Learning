class ReverseInteger:
    def reverse(x):
        rev =0
        symbol=1
        if(x<0):
            symbol=-1
            x=-x
        while(x>0):
            rem=x%10
            rev=rev*10+rem
            x=x//10
          
        return 0 if rev > pow(2,31) else rev *symbol
    print(reverse(120))