days = int(input("Enter the Days :"))
if days == 0:
   print("GOOD ,NO FINE")
elif days >=1 and days <=5:
    print("Fine Amount is", days*0.5) 
elif days > 5 and days <=10:
    print("Fine Amount is", days*2)
elif days > 10 and days <=30:
    print("Fine Amount :", days*5)
else:
    print("Your Membershipis Cancelled")            