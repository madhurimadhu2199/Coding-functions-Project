#Deleting different dictionary elements
dict1={"student1":"madhuri","student2":"diya","student3":"karthik"}
dict2={"id":int("234"),"roll":int("2"),"phoneno":int("1234567898")}
dict3={"branch1":"ECE","branch2":"CSE","branch3":"IT"}
#Deleting Specific element
del dict1["student3"]
dict2.pop("roll")
print(dict1)
print(dict2)
#Deleting all elements
del dict2
dict3.clear()
print(dict2)
print(dict3)

