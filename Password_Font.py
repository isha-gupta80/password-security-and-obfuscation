SECURE = (('I','!'),('s','$'),('h','#'),('a','@'),('i',':'))

def  passwordsecure(password):
    for a,b in SECURE:
        password = password.replace(a,b)
        
        
    return password
 
password = input("please provide your password here:")
decision = input("Do you need UPPER case letters to be present ?(Y/N)")

if decision == 'y':
    print(f"your new password is {passwordsecure(password)}")
else:
    print(f"your new password is {passwordsecure(password.lower())}")
    