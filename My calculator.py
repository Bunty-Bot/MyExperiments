#This code is made by Shreyas Bapat
print("Hello !!!! Welcome to the calculator")
operations="+","-","*","/"
def one():
    print("Enter the first number:")
    n1=int(input())
    print("Enter the second number:")
    n2=int(input())
    print("Enter the operation")
    n3=input()
    if n3=="+":
        print("The sum of two numbers is")
        print(n1+n2)
    elif n3=="-":
        print("The subtraction of two numbers is")
        print(n1-n2)
    elif n3=="*":
        print("The multiplication of two numbers is")
        print(n1*n2)
    elif n3=="/":
        print("The division of the two numbers is")
        print(n1/n2)
    return " "
def main():
    print("Do you want to perform another calculation? y or n?")
    a = input()
    if a == 'y':
        print(one())
        print(main())
    else:
        pass
    return " "

print(one())
print(main())
print("Thank you!!!! Visit again!")
