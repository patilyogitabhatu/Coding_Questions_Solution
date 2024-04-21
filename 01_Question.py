'''
Problem Description :
The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size ‘n’ as its argument ‘r’ 
represents the number of rats present in an area, ‘unit’ is the amount of food each rat consumes and each ith element of array
‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <= i

Note:

Return -1 if the array is null
Return 0 if the total amount of food from all houses is not sufficient for all the rats.
Computed values lie within the integer range.
Example:

Input:

r: 7
unit: 2
n: 8
arr: 2 8 3 5 7 4 1 2

Output:
4

Explanation:
Total amount of food required for all rats = r * unit

= 7 * 2 = 14.

The amount of food in 1st houses = 2+8+3+5 = 18. Since, amount of food in 1st 4 houses is sufficient for all the rats.
Thus, output is 4.
'''

def check_food( r, unit , n , arr):
    
    if arr is None:
        return-1
    
    food_req = r*unit
    
    ans = 0
    for i in range(0 , n):
        ans +=arr[i]
        if ans >=food_req:
            break
        
    if ans<food_req:
        return 0
    return i+1
    
r = int(input())
unit = int(input())
n = int(input())
arr = list(map(int, input().split( )))

final_ans = check_food( r, unit , n , arr)
print(final_ans)

