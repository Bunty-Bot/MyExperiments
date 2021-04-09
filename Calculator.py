#This code is made by Shreyas Bapat
#Calculator
#ALL FUNCTIONS
def greetings():
    print("Hello welcome to the calculator!!!")
    print("NOTE:- PLEASE DON'T GIVE INVALID INPUT.")
def main():
    print("Which operation do you want to perform ?\n"
          "Press 1 for Addition(+)\n"
          "Press 2 for Subtraction(-)\n"
          "Press 3 for Multiplication(*)\n"
          "Press 4 for Exponential(**)\n"
          "Press 5 for Division(/)\n"
          "Press 6 for Integer Division(//)\n"
          "Press 7 for Modulus(%)")
    n = int(input())
    if n>7:
        print("Invalid Input")
        exit()
    else:
        pass
    print("Please Type the two numbers on which\n"
          "you have to perform the operation")
    n1 = int(input())
    n2 = int(input())
    if n==1:
        print(n1+n2,"This is the sum of two numbers.")
    elif n==2:
        print(n1-n2,"This is the answer after subtraction of two numbers.")
    elif n==3:
        print(n1*n2,"This is the product of the two numbers.")
    elif n==4:
        print(n1**n2,"This is the exponential of the given number.")
    elif n==5:
        print(n1/n2,"This is the answer after the division of two numbers.")
    elif n==6:
        print(n1//n2,"This is the answer after integer division of two numbers.")
    elif n==7:
        print(n1%n2,"This is the modulus of the two numbers.")
    else:
        pass
def again():
    print("Do you want to continue calculating ?\n"
          "Press y for yes.\n"
          "Press n for no.")
    i = input()
    if i=='y':
        greetings()
        main()
        again()
    else:
        print("Thank you Visit Again!!!")
#REAL CODE
greetings()
main()
again()



