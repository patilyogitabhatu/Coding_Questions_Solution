'''
Question 4:
(Asked in Accenture OnCampus 11 Aug 2022, Slot 1)

You are given a function,
int findCount(int arr[], int length, int num, int diff);

The function accepts an integer array ‘arr’, its length and two integer variables ‘num’ and ‘diff’. Implement this function to find and return the number of elements of ‘arr’ having an absolute difference of less than or equal to ‘diff’ with ‘num’.
Note: In case there is no element in ‘arr’ whose absolute difference with ‘num’ is less than or equal to ‘diff’, return -1.

Example:
Input:

arr: 12 3 14 56 77 13
num: 13
diff: 2
Output:
3

Explanation:
Elements of ‘arr’ having absolute difference of less than or equal to ‘diff’ i.e. 2 with ‘num’ i.e. 13 are 12, 13 and 14.


'''
def findCount(arr , length ,num , diff):
    
    count = 0
    for i in arr:
        demo = abs(num - i)
        if demo <= diff:
            count +=1

    return count
        

arr = list(map(int, input().split( )))
num = int(input())
diff =  int(input())

length = len(arr)
print(findCount( arr , length , num , diff))


