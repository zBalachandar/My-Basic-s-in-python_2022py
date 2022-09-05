from unicodedata import name


class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def PrintDetails(self):
       print("Name :", self.name,"Age:",self.age)
    @staticmethod
    def welcome():
      print("Welcome to our Institutions")

T1= student("Chan",24)
T1.PrintDetails()
T1.welcome()

T2= student("selvi", 37)
T2.PrintDetails()
T2.welcome()