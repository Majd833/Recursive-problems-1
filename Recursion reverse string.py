def revstr(s):
    if len(s)==1:
        return s[0]
    first=s[0]
    return revstr(s[1:])+first
s=str(input("Enter your string:"))
print("The reverse of",s,"is",revstr(s))