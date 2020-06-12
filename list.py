#Assigning elements to different lists
Lists=[]
n=int(input("Enter the number of lists:"))
for i in range(0,n):
    count=(input())
    Lists.append(count)
print(Lists)
for j in range(0,n):
    new=Lists[j]
    k=[]
    m=int(input("Enter the list size:"))
    for j in range(0,m):
      item=int(input())
      k.append(item)
    print(new,"=",k)
