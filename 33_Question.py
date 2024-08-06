'''
Accenture slot : jul 26

Product Pair :
You are given an integer array A of length N and your task is to find and return an integer value representing the
count of unique pairs whose products are multiples of 3.

Note : A unique pair means that the elements must be the same regardless of their order for in stance,  (1,3) and (3,1)
are considered as the same pair

Input Specification :
input1 : An integer value N, representing the size of the array
input2 : An integer array A

Output Specification :
Return an integer value representing the count of unique pairs whose products are multiples of 3.

Example 1 :
input1 : 4
input2 : 3 6 5 4

output : 5

'''

N = int(input())
arr = list(map(int,input().split( )))
count = 0

for i in range(N-1):
    for j in range(i+1,N):
        pro =  arr[i]*arr[j]
        if pro % 3 == 0:
            count +=1
print(count)

            