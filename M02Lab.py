#Jack Huelskamp
#M02_Lab_Case_Study.py
#File will get students names and tell you whether they are on the  Deans list or honor roll or both


studentname = input("Enter students name ") #gets initial student name
ZZZ = "ZZZ"

while studentname != ZZZ: #runs the check to figure out what list they are on and loops back to check new students
    number = input("Enter students GPA ")
    gpa = float(number)
    if gpa >= float(3.25):
        if gpa >= float(3.50): print(studentname, "Is on the Dean's list.")
        else: print(studentname, "is on the honor roll.")
    else: print(studentname, "Is not on either list.")
    studentname = input("Enter students name ")

print("End of list of students.")