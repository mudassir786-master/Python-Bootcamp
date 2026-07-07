username = input("Enter your username:")
password = input("Enter your password:")

if username == "ADMIN":
    if password == "1234":
        print("LOGIN SUCCESSFUL")
    
    else:
     print("INCORRECT PASSWORD")
else: 
     print("INVALID USERNAME")
 
    