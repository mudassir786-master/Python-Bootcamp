marks = int(input("Enter your Marks :"))
attendance = int(input("Enter Attendance (%):"))

eligible = (marks => 35) and (attendance =>75)
print("Eligible for Exam :", eligible)
