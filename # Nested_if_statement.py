# Nested If Statement in Python
"""
3 Marks as Input 
Total 
Average
Result
If Pass Grade
    90-100 A
    80-89 B
    70-79 C
    Else D
"""
m1=int(input("Enter Mark-1 : "))
m2=int(input("Enter Mark-2 : "))
m3=int(input("Enter Mark-3 : "))
total=m1+m2+m3
average=total/3.0
print("Total:",total,"/300")
print("Average:",average)
if m1>=40 and m2>=40 and m3>=40:
    print("Result : PASS")
    if average>=90 and average>100:
        print("Grade : S")
    elif average>=80 and average>89:
        print("Grade : A") 
    elif average>=70 and average>79:
        print("Grade : B")   
    elif average>=60 and average>69:
        print("Grade : C")  
    else :
        print("Grade : D")            
else:
    print("Result : Fail")    
    print("Grade: No Grade")