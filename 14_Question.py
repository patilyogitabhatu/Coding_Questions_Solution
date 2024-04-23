'''
Question : 14
(Asked in Accenture Offcampus 2 Aug 2021, Slot 3)

Problem Statement
You are required to implement the following function:
Int Calculate(int m, int n);
The function accepts 2 positive integer ‘m’ and ‘n’ as its arguments.You are required to calculate the sum of numbers divisible both by 3 and 5, 
between ‘m’ and ‘n’ both inclusive and return the same.
Note
0 < m <= n

Example
Input:
m : 12
n : 50
Output
90

Explanation:
The numbers divisible by both 3 and 5, between 12 and 50 both inclusive are {15, 30, 45} and their sum is 90.
Sample Input
m : 100
n : 160
Sample Output
510
'''
def Calculate(m , n):
    list1 = []
    for i in range( m , n+1):
        if i % 3 == 0 and  i % 5 == 0 :
            list1.append(i)
    return sum(list1)           
    
m = int(input())
n = int(input())
print(Calculate(m,n))
