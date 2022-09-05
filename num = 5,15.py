lower = int(input("enter lower bound"))
higher = int(input("enter higher bound"))

for num in range(lower,higher+1):
    if num > 1:
        for j in range(2,num):
            if num % j ==0:
                break #not a prime number

            else:
                print(num, end=" ")
