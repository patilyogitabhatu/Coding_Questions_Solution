'''Question 3: Password Checker
(Asked in Accenture OnCampus 10 Aug 2022, Slot 3)

You are given a function.
int CheckPassword(char str[], int n);
The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
str is a valid password if it satisfies the below conditions.

– At least 4 characters
– At least one numeric digit
– At Least one Capital Letter
– Must not have space or slash (/)
– Starting character must not be a number
Assumption:
Input string will not be empty.

Example:

Input 1: aA1_67              Output 1:1
Input 2: a987 abC012         Output 2:0 
'''

def CheckPassword(str , n):
    
    di = 0
    cap = 0
    
    if n < 4 or str[0].isdigit():
        return 0
    
    
    for i in range(n):
        if str[i] == ' ' or str[i] == '/':
            return 0 
        if str[i].isdigit():
            di +=1
        if str[i] >= 'A' and str[i] <= 'Z':
            cap +=1    
            
    if di >0 and cap>0:
        return 1
    else:
        return 0
    
str = input()
n = len(str)
print(CheckPassword( str, n))
