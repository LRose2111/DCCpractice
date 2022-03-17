#Whiteboard Challenges
#1.	Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
import array as arr

arr = [5, 17, 77, 50]
target = 55
def arraytar(arr, target):
    values = dict()
    for i, elem in enumerate(arr):
        comp = target - elem
        if comp in values:
            return[values[comp], i]
        values[elem] = i 
    return[]
answer = arraytar(arr, target)
print(answer)

#2.	Palindrome is a word, phrase, or sequence that reads the same backward as forward i.e. madam. Write code that takes a user input and checks to see if it is a Palindrome and reports the result. You must handle spaces. 
def palindrome_or_not(s):
    word = ''.join(reversed(s))
    if (s == word):
        return True
    else:
        return False
s = str(input(f'Enter your word here!'))
ans = palindrome_or_not(s)
if (ans):
    print('Yes, your word is a Palindrome word!')
else:
    print('No, sorry your word is not a Palindrome word. Feel free to try again!')

#3.	Given a list of integers, return a bool that represents whether or not all integers in the list can form a sequence of incrementing integers
#a.	Use case: 
#i.	{5, 7, 3, 8, 6}  false (no 4 to complete the sequence)
#ii.	{17, 15, 20, 19, 21, 16, 18}  true



#4.	Create a method that takes an array of positive and negative numbers. Return an array where the first element is the count of the positive numbers and the second element is the sum of negative numbers. 
#a.	Use case: [7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21]







#5.	Create a method that accepts a string of space separated numbers and returns the highest and lowest number as a string
#a.	Use case: “3 9 0 1 4 8 10 2”  “0 10”


#6.	Create a method that accepts a string, check if it’s a valid email address and returns either true or false depending on the valuation. Think about what is necessary to have a valid email address.
#a.	Use case:
#i.	“mike1@gmail.com”  true
#ii.	“gmail.com”  false


#7.	Create a method that takes in a string and replaces each letter with its appropriate position in the alphabet and returns the string
#a.	Use case:
#i.	“abc”  “1 2 3”
#ii.	“coding is fun”  “3 15 4 9 14 7 9 19 6 21 14”


#8.	A briefcase has a four-digit rolling-lock. Each digit is a number from 0-9 that can be rolled either forwards or backwards. Write a method that returns the smallest number of turns it takes to transform the lock from current combination to the target combination. One turn is equivalent to rolling a number forwards or backwards by one. 
#a.	Use case: 
#i.	Current lock: 3893
#ii.	Target lock: 5296


#9.	Happy Numbers
#a.	A happy number is a number defined by the following process: starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1. An example of a happy number is 19


#10.	Given a number, return the reciprocal of the reverse of the original number, as a double. 
#a.	Use case: If given 17, return 0.01408 (1/71)
