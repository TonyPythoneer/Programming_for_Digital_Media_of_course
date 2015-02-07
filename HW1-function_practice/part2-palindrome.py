def palindrome(s):
    x=0
    y=len(s)-1
    while x<len(s):
        if not s[x]==s[y]:
            return False
        print s[x],s[y]
        x=x+1
        y=y-1        
    return True

def have_alphabetic(s):
    x=0
    while x<len(s):
        if s[x]>""==s[y-1]:
            return False
        x=x+1
        y=y-1
    return True

s=raw_input("Enter a string!")
s= s.replace(' ','')
if palindrome(s):
    print("It is a palindrome!")
else:
    print("It is not a palindrome!")
