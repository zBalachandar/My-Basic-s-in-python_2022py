""""
class student():
    Name:"New"
    ages:8.9
    operations:67

def printall():
    print("Name :", student.Name)
    print("ages :", student.ages)

student.printall()
print(student__dict__)
"""
"""""
class user:
    def __init__(self, name, age):
       self.name = name
       self.age  = 24
       self.msg=self.name+"is"+str(self.age) + "years old"
o = user("Newbie", 45)      
print(o.name) 
print(o.age) 
print(o.msg) 

"""
"""
class student:
    def __init__(self,total):
       self.total=total
    def average(self):   
     return self.total / 4.0

o = student(7000)   
print("Total :",o.total)
print("Average:", o.average())
"""
class student:
    count=0
    def __init__(self,name,age):
      self.name=name
      self.age=age
      student.count +=1

    def PrintDetails(self):  
      print("Name :", self.name, "Age:",self.age)
    @classmethod
    def total(cls):
        return cls.count

o =student("James",25)
o.PrintDetails()

o =student("Roger",27)
o.PrintDetails()
print("Total Admissions :", student.total())

