'''
Question:13
(Asked in Accenture Offcampus 2 Aug 2021, Slot 2)

Problem Statement
You are given a function,
Int MaxExponents (int a , int b);
You have to find and return the number between ‘a’ and ‘b’ ( range inclusive on both ends) which has the maximum exponent of 2.
The algorithm to find the number with maximum exponent of 2 between the given range is
Loop between ‘a’ and ‘b’. Let the looping variable be ‘i’.
Find the exponent (power) of 2 for each ‘i’ and store the number with maximum exponent of 2 so faqrd in a variable ,
let say ‘max’. Set ‘max’ to ‘i’ only if ‘i’ has more exponent of 2 than ‘max’.
Return ‘max’.
Assumption: a <b

Note: If two or more numbers in the range have the same exponents of  2 , return the small number.

Example
Input:
7
12
Output:
8
Explanation:

Exponents of 2 in:
7-0
8-3
9-0
10-1
11-0
12-2
Hence maximum exponent if two is of 8.
'''

def MaxExponents(a, b):
    max_exponent = 0
    max_num = a
    for i in range(a, b + 1):
        exponent = 0
        num = i
        while num % 2 == 0:
            num //= 2
            print(num)
            exponent += 1
        print("________")    
        if exponent > max_exponent:
            max_exponent = exponent
            max_num = i
    return max_num

# Example usage:
a = int(input())
b = int(input())
result = MaxExponents(a, b)
print(result)

