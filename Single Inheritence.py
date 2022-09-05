"""""
class Nokia:
   company = "Nokia china"
   website = "www.nokia.china.com"

   def contact_details(self):
    print("Address: Niyagara Road, China Highways,China-0897878")

class Nokia2700c(Nokia):
    def __init__(self):
        self.name = "Nokia2700c"
        self.year = 2011

    def product_details(self):
      print("Name :",self.name)
      print("Year :",self.year)
      print("company :",self.company)
      print("Website :",self.website)

mobile = Nokia2700c()
mobile.product_details()
"""
"""
class Grandfather:
    def ownhouse(self):
        print("GrandFather House")

class Father(Grandfather):
    def ownbike(self):
        print("Father have a ownbike") 

class Son(Father):
    def ownbook(self):
        print(" SON Have a own book")              


o = Son()
o.ownhouse()
o.ownbook()
"""

try:
  file=open(w"C:\Users\S.ELUMALAI\Desktop\yuor.txt")
  #print(file.readline())
  print(file.readlines())
  #(file.write("This is chandru, and coming for my amma selvi"))
  file.close()
  file=open(r"C:\Users\S.ELUMALAI\Desktop\yuor.txt")
  for line in file:
    print(line)

except FileNotFoundError:
    print("Error:Sorry bro this file is not found ,Right Now")
else:
    file.close()    