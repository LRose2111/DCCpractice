#1. Happy Numbers
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
for number in range(1, 101):
    count = 0
    for i in range(2, (number//2 + 1)):
        if(number % i == 0):
            count = count + 1
            break        
    if(count == 0 and number != 1):
        print(number, end='   ')
    
#3. Fibonacci
n1 = 0
n2 = 1 
fibon = [n1, n2]

for i in range(0, 10):
    n3 = n1 + n2
    fibon.append(n3)
    n1 = n2
    n2 = n3

print(fibon)


