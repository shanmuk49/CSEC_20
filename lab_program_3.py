# program 3.1

height = int(input("Enter The Triangle Height : "))
for i in range(1, height + 1 ):
    print("*" * i, end='\n')

for i in range(1,height+1):
    for j in range(1,i+1):
        print("*", end='')
    print(" ")

'''
Expected Output :
*
**
***
****
*****
* 
** 
*** 
**** 
*****

# 3.2 program

import random
rand = random.randint(1, 10)
#print("Random value = ", rand)
guess = int(input("Guess The Number : "))
if guess == rand:
    print("Yes,You guess is correct ")
else:
    print("No, Your guess is wrong ")

'''
Expected Output :
Guess The Number : 5
No, Your guess is wrong 
'''

# program 3.3
num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))
print(num1, num2, num1 - num2)
difference = float(f'{abs(num1 - num2):.3f}')
print(difference)
print('Close' if difference <= 0.001 else 'Not Close')

'''
Expected Output :
Enter First Number : 53.36
Enter Second Number : 46.34
53.36 46.34 7.019999999999996
7.02
Not Close
'''