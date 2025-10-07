import math

#1
n = input("Enter a number: ")
reversed = "".join(reversed(n))
print("Reversed number:", reversed)

#2
n = input("Enter two numbers: ")
n = n.split()
print(f"Reversed: {n[1]} {n[0]}")

#3
n = int(input("Enter a number: "))
if n & (n-1) == 0:
    print("True")
else:
    print("False")

#4
a, b = input("Enter two numbers: ").split()
ans = int(a) // int(b)
print("The quotient is:", ans)

#5
a, b = input("Enter two numbers: ").split()
ans = int(a) / int(b)
print(f"The quotient is: {math.ceil(ans)}")

#6
x = int(input("Enter a number: "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

#7:
a, b = input("Enter two numbers: ").split()
if int(a) and int(b) < 0:
    print("Yes")
else: 
    print("No")

#8
a, b = input("Enter two strings: ").split()
if len(a) > len(b):
    print(True)
else:
    print(False)

#9
a,b,c = input("Enter three numbers: ").split()
if int(a) + int(b) > int(c) and int(a) + int(c) > int(b) and int(b) + int(c) > int(a):
    print("Yes")
else: 
    print("No")

#10
num = input("Enter four numbers: ").split()
largest = 0
for i in num:
    if int(i) > int(largest):
        largest = i 
print(largest)

#11
a,b,c = input("Nhập ba số nguyên dương: ").split()
if int(a) + int(b) > int(c) and int(a) + int(c) > int(b) and int(b) + int(c) > int(a):
    if int(a) == int(b) == int(c):
        print("Tam giác đều")
    elif int(a) == int(b) or int(a) == int(c) or int(b) == int(c):
        print("Tam giác cân")
    else:
        print("Tam giác thường")
else: 
    print("Không phải tam giác")

#12
year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Yes")
else:
    print("No")

#13
money = int(input("Nhập số kWh điện đã tiêu thụ: "))
if money > 100:
    total = 50*1500 + 50*2000 + (money-100)*3000
elif 50 < money <= 100:
    total = 50*1500 + (money-50)*2000
else:
    total = money * 1500
print(total)

#14
a,b = input("Nhập hai số a,b trong phương trình ax + b = 0: ").split()
try:
    x = -float(b)/float(a)
    x = round(x, 2)
    print(f"Phương trình có nghiệm x = {x}")
except ZeroDivisionError:
    if float(a) == float(b) == 0:
        print("Vô số nghiệm")
    else:
        print("Vô nghiệm")

#15
hocluc = float(input("Nhập học lực: "))
if hocluc < 5:
    print("Yếu")
elif 5 <= hocluc < 6.5:
    print("Trung bình")
elif 6.5 <= hocluc < 8:
    print("Khá")
elif 8 <= hocluc:
    print("Giỏi")

#16
number = input("Enter a number: ")
number = list(number)

#Tách số thành 2 phần: trước dấu phẩy và sau dấu phẩy
for i in number:
    if i == "." or i == ",":
        a = number[:number.index(i)]
        b = number[number.index(i)+1:]
        a = "".join(a)
        b = "".join(b)
        
#Làm tròn số tới số nguyên gần nhất: Nếu số sau dấu phẩy >= 5 => làm tròn lên, ngược lại làm tròn xuống
        if int(b[0]) >= 5:
            round = int(a)+1 if int(a)>=0 else int(a)-1 
        else:
            round = int(a)
            
#Làm tròn lên/xuống với số âm/dương        
        if int(a) >= 0:
            if int(b)==0:
                print(int(a), int(a), round)
            else:
                print(int(a)+1, int(a), round)
        else:
            if int(b)==0:
                print(int(a), int(a), round)
            else:
                print(int(a), int(a)-1, round)

#17
a,b,c = input("Nhập ba số nguyên dương: ").split()
if int(a) + int(b) > int(c) and int(a) + int(c) > int(b) and int(b) + int(c) > int(a):
    if int(a) == int(b) == int(c):
        print("Tam giác đều")
    elif int(a) == int(b) or int(a) == int(c) or int(b) == int(c):
        print("Tam giác cân")
    else:
        print("Tam giác thường")
else: 
    print("Không phải tam giác")