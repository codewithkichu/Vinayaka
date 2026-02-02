#Students Grade Report

n = int(input("Enter the number of students"))

count_A = 0
count_B = 0
count_C = 0
count_F = 0

for i in range(1,n + 1):
    marks = int(input(f"Enter the marks of students {i}:"))
    if marks >= 90:
        print("Students",i,"Grade:A")
        count_A += 1
    elif marks >=75:
        print("Student" , i ,"Grade:B" )
        count_B =+ 1
    elif marks >=50:
        print("Students" ,i,"Grade:C")
        count_C += 1
    else:
        print("Student",i,"Grade:Fail")
    count_F += 1

print("\n---Grade Summary---")
print("A Grade:",count_A)
print("B Grade:",count_B)
print("C Grade:",count_C)
print("Fail",count_F)


