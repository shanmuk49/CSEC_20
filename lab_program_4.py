# 4.1 program

word = input("Enter A Word : ")
flag = 0
for ch in word:
    if ch in 'aeiouAEIOU':
       flag+=1
       break
if flag == 1:
    print(f'{word} contains vowels')
else:
    print(f'{word} contains no vowels')


'''
Expected  Output :
Enter A Word : Aditya
Aditya contains vowels
'''


# 4.2 program

str1 = input("Enter First String : ")
str2 = input("Enter Second String : ")
L1 = len(str1)
L2 = len(str2)
if L1 != L2:
    print(f'len({str1}) = {L1} and len({str2}) = {L2}')
else:
    str = ''
    for i in range(L1):
        str += str1[i] + str2[i]
    print(str1, str2, str)

'''
Expected Output : 
Enter First String : Mastan
Enter Second String : sunila
Mastan sunila Msausntialna
'''


# 4.3 program




# 4.4 program

expression = input("Enter Your Expression : ")
print(expression)
convert_expression = ''
for i in range(len(expression) - 1):
    if expression[i].isalnum() and (expression[i+1].isalpha() or expression[i+1] == '('):
        convert_expression += expression[i] + '*'
    elif expression[i] == ')' and expression[i+1] == '(':
        convert_expression += expression[i] + '*'
    elif expression[i] == ')' and expression[i+1].isalnum():
        convert_expression += expression[i] + '*'
    else :
        convert_expression += expression[i]
convert_expression += expression[i+1]
print(convert_expression)

'''
Expected Output : 
Enter Your Expression : ab+cd
ab+cd
a*b+c*d
'''
