'''
Accenture slot : jul 26 2024

Even Sum :
You are organizing a charity run where participants contribute a doller for every even-numbered kilometer they complete.
your task is to find and return an integer value representing the total amount of money raised if the race is N km long.

Input Specification :
input 1 : An integer value N

Output Specification :
Return the sum of all even numbered kilometer till N they complete.

Example 1 :
input1 : 10 
output1 : 30

Explanation :
Here, N=10. The even numbers between 1 and 10 are 2,4,6,8,10,and their sum will be 30. Hence , 30 is returned as the output

Example 2 :
input1 : 7
output1:12
'''

N = int(input())
listeven = []

for i in range(N+1):
    if (i%2) == 0:
        listeven.append(i)
        
result = sum(listeven)
print(result)
