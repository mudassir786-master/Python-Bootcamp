age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen? (YES/NO): ")

if age >= 18:
   if citizen == "YES":
    print("YOU ARE ELIGIBLE FOR VOTING")
   else:
    print("YOU MUST BE AN INDIAN CITIZEN")
else:
    print("YOU ARE NOT ELIGIBLE FOR VOTING")
