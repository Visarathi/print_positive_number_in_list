myList=[]
a = eval(input("enter the no. of elements in the list:\n"))                                 
for i in range(0,a):
    print("enter the element no.\n",i)
    i+=1
    element=int(input())
    myList.append(element)

print("Enter the list\n",myList)
print()

if(element>=0):
    myList.append(element)
    print(myList)
