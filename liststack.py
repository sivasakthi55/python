#list stack
'''
liststack=[3,2,1]
print(liststack)

liststack.append(5)
print(liststack)

liststack.append(6)  
print(liststack)

liststack.pop()
print(liststack)


#list queue

from collections import deque

queue=deque(["apple","orange","kiwi"])
print(queue)

queue.append("banana")
print(queue)

queue.popleft()
print(queue)

#del

a=[1,2,3,4,5,6,7,8]

print(a)

del a[0]
print(a)

del a[2:3]
print(a)

del a[ : ]
print(a)

del a
print(a)



name=[]

for i in range(3):
 name.append(str(input("enter a name:")))
print(name)

name.pop()
print(name)

'''


from collections import deque 

queue=deque([str(input("enter a fruits:"))])
for i in range(3):
 queue.append(str(input("enter a fruits:")))

print(queue)

queue.popleft()
print(queue)






