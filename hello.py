#!/usr/bin/env python2

# Python Program - Make Simple Calculator

print "1. Addition"
print "2. Subtraction"
print "3. Multiplication"
print "4. Division"
print "5. Exit"
CHOICE = int(input("Enter your choice: "))
if (CHOICE >= 1 and CHOICE <= 4):
    print "Enter two numbers: "
    NUM1 = int(input())
    NUM2 = int(input())
    if CHOICE == 1:
	RES = NUM1 + NUM2
	print("Result = ", RES)
    elif CHOICE == 2:
	RES = NUM1 - NUM2
	print("Result = ", RES)
    elif CHOICE == 3:
	RES = NUM1 * NUM2
	print("Result = ", RES)
    else:
	RES = NUM1 / NUM2
	print("Result = ", RES)
elif CHOICE == 5:
    exit()
else:
    print "Wrong input..!!"
