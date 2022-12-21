#Assignment1
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

#ASSIGNMENT2
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

#assignmet3
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



