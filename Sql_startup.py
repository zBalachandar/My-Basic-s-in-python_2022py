import sqlite3
con = sqlite3.connect('busy.db')

def insertData(name,age,city):
    qry="insert into busy (NAME,AGE,CITY) values (?,?,?);"
    con.execute(qry,(name,age,city))
    con.commit()
    print("User Details Added")

print("""
    1.Insert
    2.Update
    3.Delete
    4.Select
    """)

ch=1
while ch==1:
    c=int(input("Enter your choice :"))
    if c==1:
        print("Enter your new Record")
        name=input("Enter Name : ")
        age=input("Enter your age : ")
        city=input("Enter your city : ")
        insertData(name,age,city) 
    elif c==2:
        print("Edit A Record")
        id = input("Enter ID : ")
        name=input("Enter Name : ")
        age=input("Enter your age : ")
        city=input("Enter your city : ")

        updateData(name,age,city,id)
    elif c==3:
        print("Delete your Record")
    elif c==4:
        print("Print all Record")   
    else:
        print("Please enter a valid key")     
    ch=int(input("Enter 1 to continue : "))    
print("Thank you")