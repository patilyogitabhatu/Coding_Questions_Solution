'''
TCS Digital
Day 1 Slot 1
Question 1
Problem Description -: Given an array Arr[ ] of N integers and a positive integer K. The task is to cyclically rotate the array clockwise by K.
Note : Keep the first of the array unaltered. 

Example 1:

5  —Value of N
{10, 20, 30, 40, 50}  —Element of Arr[ ]
2  —–Value of K
Output :
40 50 10 20 30

Example 2:

4  —Value of N
{10, 20, 30, 40}  —Element of Arr[]
1  —–Value of K
Output :
40 10 20 30
'''
N = int(input())
arr = list(map(int , input().split()))
k = int(input())
for i in range(k):
    last = arr[-1]
    j = len(arr)-1
    while j !=0:
        arr[j] = arr[j-1]
        j -=1 
        
    arr[0]=last
print(arr)     
    