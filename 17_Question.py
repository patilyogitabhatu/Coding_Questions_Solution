'''
Question : 17
Instructions: You are required to write the code. You can click on compile and run anytime to check compilation/execution status.
The code should be logically/syntactically correct.

Question: Write a program such that it takes a lower limit and upper limit as inputs and print all the intermediate palindrome numbers.

Test Cases:

TestCase 1:
Input :
10 , 80
Expected Result:
11 , 22 , 33 , 44 , 55 , 66 , 77.

Test Case 2:
Input:
100,200
Expected Result:
101 , 111 , 121 , 131 , 141 , 151 , 161 , 171 , 181 , 191.
'''
def checkPalindrome(no):
    num = str(no)
    revnum = num[::-1]
    
    return num==revnum
        
num1 =int(input())
num2 =int(input())
result = []
for i in range(num1 , num2+1):
    if checkPalindrome(i):
        result.append(i)
print(result)    
        
        