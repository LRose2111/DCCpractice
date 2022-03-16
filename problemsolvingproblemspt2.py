#1. Happy Numbers a. https://en.wikipedia.org/wiki/Happy_number
answer = int(input(f'Enter number to see if happy/sad!'))
previous_numbers = []
while True:
    if answer == 1:
        print('Number is happy!:)')
        break
    answer = sum(int(c)**2 for c in str(answer))
    if answer in previous_numbers:
        print('Number is sad!:(')
        break
    else: 
        previous_numbers.append(answer)

#2. Prime Numbers
#a. A prime number is a number that is only divisible by one and itself.
#b. Write a method that prints out all prime numbers between 1 and 100
for number in range(1, 101):
    count = 0
    for i in range(2, (number//2 + 1)):
        if(number % i == 0):
            count = count + 1
            break        
    if(count == 0 and number != 1):
        print(number, end='   ')
    
#3. Fibonacci
#a. A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
#b. Write a method that does the Fibonacci sequence starting at 1
#c. HARDER VERSION: Write a method that does the Fibonacci sequence starting at a number that a user inputs


