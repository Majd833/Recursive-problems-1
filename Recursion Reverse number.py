def revnum(num):
    if num>0:
        last=num%10
        if num//10>0:
            curnum=revnum((int)(num//10))
            return last*pow(10,len(str(curnum)))+curnum
        return num
n= int(input("Enter your number:"))
print("The reverse of",n,"is",revnum(n))