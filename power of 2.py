def power2(n):
    if n<=0:
        return False
    if n==1:
        return True
    if n%2==0:
        return power2(n/2)
n=int(input("Enter yout number;"))
if power2(n):
    print("It is a power of 2")
else:
    print("Your number is not a power of 2")