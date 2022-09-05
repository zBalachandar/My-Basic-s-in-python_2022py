
a=[1,2,3,4,5,6,7]
print(a[5])
a[4]=900
print(a[4])

print("---------------------------")

a=[0,True,'Selvi',1.45,{1,2,2,4,6,7,7},[1,2,44,567,886]]
print(type(a))
print(a[0],"Type is",type(a[0]))
print(a[2],"Type is",type(a[2]))
print(a[4],"Type is",type(a[4]))
print(a[5],"Type is",type(a[5]))
a =[1,4,5,7,8,9]
print(a)
a.clear()
print(a)
print("------------------------------------------------")
a=[1,2,3,4,5,7,8,9,9,9,0]
b=a.copy()
print("B =",b)
print(a.index(9))
a.pop(4)
print(a)
a.remove(3)
print(a)
print("--------------------------------------------------------------")
a=["Ramu"]
print(a)
a.append("Selvi")
a.append("Chandu")
a.append("God")
print(a)
a1=["Nagaraj","Avinash","IAS"]
a.extend(a1)
print(a)
a.insert(5,"Chan")
print(a)
print("--------------------------------------------------------------")

A=[1,4,66,879,00,435,657885,867654,43223]
print(A)
A.sort(reverse=True)
print(A)