# ID : 20CE048
# Name : Maharshi Limbachiya

# AIM: 
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

# Input Format: The first line contains. The second line contains an array A[]  of n integers each separated by a space.

# Constraints:
# Output Format: Print the runner-up score.

# Sample Input

# 5
# 2 3 6 6 5

# Sample Output

# 5

# Explanation: Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.

# github repository link : https://github.com/Maharshi04/Python-Practical/blob/main/Pract4.py

n=int(input())
a=list(map(int, input().split()))
mx=max(a[0],a[1])
secondmax=min(a[0],a[1])

for i in range(2,len(a)):
    if a[i]>mx:
        secondmax=mx
        mx=a[i]
    elif a[i]>secondmax and \
        mx != a[i]:
        secondmax=a[i]
 
print(secondmax)