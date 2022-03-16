#1. Reverse a string
word = 'baseball'
for index in range(len(word) -1, -1, -1):
    print(word[index])

#2. Capitalize letter
word = 'i love duck hunting'

u = word.title()
print(u)

#3. Compress a string of characters
string = ''
word = 'usssssssmmmmmmmccccc'
count = 1
for i in range(len(word)-1):
    if word[i] == word[i+1]:
        count = count + 1
    else:
        string = string + word[i] + str(count)
        count = 1
string = string + word[i+1] + str(count)
print(string)

#4. BONUS CHALLENGE: Palindrome
word = 'civic'
for index in range(len(word) -1, -1, -1):
    print(word[index])
user_input = input(f'Is {word} spelt the same backwards as it is foward? (Y/N)')
if user_input == 'Y':
    print('Yes! Great job!')
if user_input == 'N':
    print('Are you sure? Check again!')
