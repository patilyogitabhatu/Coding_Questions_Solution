'''
Question:10
(Asked in Accenture Offcampus 1 Aug 2021, Slot 2)

Problem Statement

A carry is a digit that is transferred to left if sum of digits exceeds 9 while adding two numbers from right-to-left one digit at a time
You are required to implement the following function.
Int NumberOfCarries(int num1 , int num2);
The functions accepts two numbers ‘num1’ and ‘num2’ as its arguments. You are required to calculate and return  the total number of carries generated 
while adding digits of two numbers ‘num1’ and ‘ num2’.
Assumption: num1, num2>=0

Example:
Input
Num 1: 451
Num 2: 349
Output
2
Explanation:

Adding ‘num 1’ and ‘num 2’ right-to-left results in 2 carries since ( 1+9) is 10. 1 is carried and (5+4=1) is 10, again 1 is carried. Hence 2 is returned.

Sample Input
Num 1: 23
Num 2: 563
Sample Output
0
'''

def  NumberOfCarries(num1 , num2):
    str1  = str(num1)
    str2  = str(num2)

    if len(str1) != len(str2):
        max_length = max(len(str(num1)), len(str(num2)))

        # Pad the numbers with zeros to make them the same length
        str1 = str(num1).zfill(max_length)
        str2 = str(num2).zfill(max_length)

    count = 0
    a = 0
    length = len(str1)-1
    
    while length >=0:
        
        a = int(str1[length]) + int(str2[length]) + int(str(a)[0])
        print("A:",a)
        if len(str(a)) > 1:
            count +=1
        else:
            a=0    
            
        length -= 1 
    return count    
            

num1 = int(input())
num2 = int(input())

print(NumberOfCarries(num1 , num2))