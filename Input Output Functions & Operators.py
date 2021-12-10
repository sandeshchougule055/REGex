# Name = Sandesh Chougule

# Referral id = DIRSS2136

#Assign 1

#Accept..Student details with 5 marks
#Total
#Average

#Display total and average along with all student details

sname = input("Enter student name : ")
sci = int(input("enter Science marks : "))
maths = int(input("enter Maths marks : "))
eng = int(input("enter English marks : "))
history = int(input("enter History marks : "))
hindi = int(input("enter Hindi marks : "))
total = (sci + maths + eng + history + hindi)
print(total)
average = (total)/5
print(average)

print("*******************************************************")

#Assign 2

#Accept 3 number from user
#	Calculate
#			Addition
#			Subtraction
#			Multiplication

s = int(input("enter first value : "))
P = int(input("enter Second value : "))
Q = int(input("enter Third value : "))
Add = s+P+Q
Sub = s-P-Q
Mul = s*P*Q
print("the Addition of three numbers is : ",Add)
print("the Subtraction of three numbers is : ",Sub)
print("the Multiplication of three numbers is : ",Mul)

print("*******************************************************")

#Assign 3

#Accept employee details from user using input function
#	Empname
#	Empdesg
#	Empsal
#	Empexp
#Calculate 15% hike to employee

Ename = input("Enter Employee Name : ")
Edesg = input("Enter Employee Design : ")
old_Sal = int(input("Enter Employee old Salary : "))
hike = int(input("Enter your hike Percentage : "))
Eexp = input("Enter Employee Experience : ")
pre_Sal = old_Sal + (old_Sal + hike/100)

print("**************************")

print("Employee Name is : ",Ename)
print("Employee Design is : ",Edesg)
print("Employee Salary is : ",old_Sal)
print("After hike present Salary is : ",pre_Sal)
print("Employee Experience is : ",Eexp)

print("*******************************************************")

# Assignment 4:

# take 4 digit number from user & print actual & reverse format

num = int(input("enter Four digit number : "))
slice1 = str(num)
print((slice1)[::-1])
print("********************************************")
print("reverse order : ")
print(slice1[-1])
print(slice1[-2:-3:-1])
print(slice1[-3:-4:-1])
print(slice1[-4::-1])
print("********************************************")
print(slice1[:1:])
print(slice1[1:2:])
print(slice1[2:3:])
print(slice1[3::])
print("********************************************")

print("*******************************************************")

# Assign 5

# Take a fruit name from user try to display the individual characters of fruit name

fruit=input("enter the fruit name : ")
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])
print(fruit[4])
print(fruit[5])


