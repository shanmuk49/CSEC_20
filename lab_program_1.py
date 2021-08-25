# program 1.1

fweight = float(input("Enter weight In Kilograms : "))
fpounds = fweight * 2.2
print(f'{fweight} Kilograms = {fpounds: .2f} Pounds')
print(str(fweight)+" Kilograms = " +str(fpounds)+ " Pounds")

''' 
Expected Output:
Enter weight In Kilograms : 5
5.0 Kilograms =  11.00 Pounds
5.0 Kilograms = 11.0 Pounds
'''

# program 1.2

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))
total = num1 + num2 + num3
average = total / 3
print(f'{num1} + {num2} + {num3} = {total}')
print(f'Average({num1}, {num2}, {num3}) = {average : .2f}')
print("Total = ", total, "Average = ", average)

'''
Expected Output:
Enter First Number : 5
Enter Second Number : 5
Enter Third Number : 6
5 + 5 + 6 = 16
Average(5, 5, 6) =  5.33
Total =  16 Average =  5.333333333333333
'''