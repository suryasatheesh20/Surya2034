#write a function to check whether it is palindro
"""
def palindrome(n):
    for i in range(0,int(len(n))/2):
        if n[i]!=n[len(str)-i-1]:
            return False
        return True
    n='malayalam'
    ans=palindrome(n)
    if(ans):
        print("its palindrome")
    else:
        print("its not palindrome")

#Assignment
#write a pgm that accepts a setence and calculate
#calculate the no of lettersand digits
#suppose the following input is supplied to the program
#then,the output should be:
#LETTER 10
#Digits 3
s=input('enter a string:')
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
       pass
print("LETTERS:",l)
print("DIGITS:",d)

#ASSIGNMENT
#The pgm will first randomly generate a number
#unknown to the user.the user need to gues what,
#that no is.if the users guess is wrong,
#the pgm should return some sort of indication
#as to how wrang(eg the no is tooo high or too low)
#if the user guessess correctly,a positive indication should appear
#maximum of 5 tries.you will needfunctions tocheck if
#the user input is an actual no,to see the diffe bw the input no and the random
import random
number = random.randint(1, 10)

player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))


# given a list L and an interger n,rotate L to the right by n places
#if n is negative rotate L to the left by n places
#example
#L=[1,2,3,4,5,6,7,8,9,10]
#if n is 3 then L=[8,9,10,1,2,3,4,5,6,7]
#if n is -3 then L=[4,5,6,7,8,9,10,1,2,3]

#with function

def rotate(L,n):
    if n==0:
        return
    if n>0:
        for i in range(n):
            x=L.pop()
            L.insert(0,x)
    else:
        for i in range(-n):
            x=L.pop(0)
            L.append(x)
L=[1,2,3,4,5,6,7,8,9,10]
n=int(input("enter an integer"))
rotate(L,n)
print(L)

#withoput function #uses slicing in it
myList =[5, 20, 34, 67, 89, 94, 98, 110]
print("List before rotation = ",myList)
n=int(input("input an number"))
# Rotating the List
myList=(myList[-n:]+myList[:-n])
print("Updated List after rotation = ",myList)



# Assignment-2------Using function
# fibonacci sequence is 1,1,2,3,5,8,13,21...
#given a n ,write a function to return n numbers of fibonacci sequence

def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

n=int(input("enter an integer"))
for i in range(n+1):
    print(Fibonacci(i))


#Assignment-3------Using function
#write a function to check whether it is palindrome

def is_palindrome(str):
    if str==str[::-1]:
        return True
    else:
        return False
n=input("enter an string")
print(is_palindrome(n))

#create a class
#class [space]: classnamr
class employee:
    empcount=0
    #defining constructor
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        employee.empcount=employee.empcount+1
    def displayemployee(self):
        print('name:',self.name,'age:',self.age,'salary',self.salary)
        #create an object
    def displaycount(self):
        print('total no of employee',employee.empcount)
employee1=employee('faith',23,2000)
employee1.displayemployee()
employee2=employee('python',45,30000)
employee2.displayemployee
employee2.displayemployee()
employee2.displaycount()
#oops exercise
#create a class oop,constructor with the parameter such as age,name
#create two method sit() and rollover() and tellage()
#create objects and print the actions
3object.sit()#o/p{dogname} is siting
#object.rollover()#o/p {dogname}is rolled over
#object.tellage()#o/p {dogage}the age is 9
class Dog
    def __int__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name,'is sitting')
    def rollover(self):
        print(self.name,'is rolled over')
    def tellage(self):
        print(self.name,'the age is 9',self.age)

#oops-inheritance demo
#deriving a subclass from base class with all the variables and member functions
class Rocket:
    #define the constructor
         def __init__(self,name,distance):
             self.name=name
             self.distance=distance
#defining a member fun for the base class
         def launch(self):
             message="%s has reached %s"%(self.name,self.distance)
             return message
#define asub/inherited class inherits from rocket
#syntax:subclassname(baseclassname)
class Pslv(Rocket):
    #define the constructor of the subclass
         def __init__(self,name,distance,maker):
            Rocket.__init__(self,name,distance)
#passing the name and distance tothe parent constructor
            self.maker=maker
         def get_maker(self):
             makermessage="%s is at the distance %s was lounched by %s"%(self.name,self.distance,self.maker)
             return makermessage
#create object for the subclass
P1=Pslv('k','j','m')
msg1=P1.get_maker()
print(msg1)
msg2=P1.launch()
print(msg2)
#create a class animal with speak() method
#create a class dog inherit from animal
#and create a method bark()
#create a class dog child inherit from dod and
#create a mothod eat()
#create a object of dogchild() and access all the mothods
class animal:
    def speak(self):

#Demostration without encapsulation
class person:
#defining the consturctor
      def __init__(self,name,age):
          self.name=name
          self.__age=age
#defining memberfunction
      def display(self):
          print(self.name)
          print(self.__age)
      def setAge(self,age):#setter method to change age
          self.__age=age
      def getAge(self):
          return self.__age
personobj=person('su',7)
personobj.display()#is possible
#print(personobj.name,personobj.age)is not possible bz its private function
personobj.setAge(50)
personobj.display()

#polymorphism
#function overloading
#def product(a,b)
# return a*b
#def product(a)
#return a*b#function with same name and

class Bird():
    def intra(self):
        print('there are many type ofbirds')
    def flight(self):
        print('most of the birds can fly but..')
class sparrow(Bird):
    def flight(self):
        super().flight()
        print('sparrow can fly')
class astrich(Bird):
    def flight(self):
        print('ostriches...')
p=Bird()
p.flight()
a=sparrow()
a.flight()
"""















