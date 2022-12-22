#ASSIGNMENT1calculator
"""
class calc():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("sum:",self.a+self.b)
    def mul(self):
        print("mul:",self.a*self.b)
    def div(self):
        print("div:",self.a/self.b)
    def sub(self):
        print("sub:",self.a-self.b)
a=int(input("enter first no:"))
b=int(input("enter second no:"))
obj=calc(a,b)
obj.add()
obj.sub()
obj.div()
obj.mul()

#ASSIGNMENT2
#WRITE A FUNCTION THAT TAKE two sentence
#split the words by space and create two lists of wods
#elements that are common to both the list

#fistelement=['hellow','python']
#secondelement=['hello','faith']
#duplicate=['helo']
#withoutduplicate=['python','faith']
a=input('enter the sentance')
b=input('enter the sentence')
list1=a.split(" ")
print(list1)
list2=b.split(" ")
print(list2)
new_list=[]
for i in list1:
    for x in list2:
        if i==x:
            new_list.append(i)
print('new_list is',new_list)
new_list1=[]
for k in list1:
    if k not in new_list:
        new_list1.append(k)
for r in list2:
    if r not in new_list:
        new_list1.append(r)
print('the list without duplicate',new_list1)
"""


