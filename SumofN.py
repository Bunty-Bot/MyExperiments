#This code is made by Isha Kotasthane
#Sum of N number

print("Please enter the number upto which you want the sum:")
n = int(input())
def findsum(n):
    sum = 0
    i = 1
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum


print(findsum(n))