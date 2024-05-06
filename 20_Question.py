'''
TCS NQT Coding Question 2023 – September Day 1 – Slot 1
Problem Statement –

Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit assignment problems before the lecture. Today he got one tricky question. The problem statement is “A positive integer has been given as an input. Convert decimal value to binary representation. Toggle all bits of it after the most significant bit including the most significant bit. Print the positive integer value after toggling all bits”.

Constrains-

1<=N<=100

Example 1:

Input :

10  -> Integer

Output :

5    -> result- Integer

Explanation:

Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which represents “5”. Hence output will print “5”.
'''
n = int(input())
binary = str(bin(n))[2:]
new_no = ""

for i in binary:
    if i == '1':
        new_no = new_no + '0'
    elif i == '0':
        new_no = new_no + '1'
        
result = int(new_no , 2)
print(result)