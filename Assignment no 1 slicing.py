# Name : Sandesh Chougule
# Referral Id : DIRSS2136

# Assignment No 1 :

# Extract the FRUIT name only.

s="APPLEFRUITBANNANAFRUITKIWIFRUITMANGOFRUIT"
s1=s.split("FRUIT")
print(s1)

print("****************************************")

# Assignment No 2 :

# print first name ,last name, domain  from given String.

emailid = "sandesh.chougule@gmail.com"
p=emailid.split(".",1)
res=p[1]
q=res.split("@")
print(p[0])
print(q[0])
print(q[1])

print("****************************************")

# Assignment No 3 :

# print first name ,last name, age, domain,birth year  from given String.

A = "sandesh.chougule.1998@gmail.com"
B = A.split(".",1)
print("First Name : ",B[0])
C = B[1]
print("Last Name : ",C[0:9])
print("Birth Year : ",C[9:13])
print("Age : ",2021-int(C[9:13]))
print("Domain : ",C[-9: ])


