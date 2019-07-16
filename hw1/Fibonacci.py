#A program that returns the nth number in the Fibonacci sequence

n = eval(input("Enter 'n' to find the nth term in Fibonacci's sequence: "))# ask which 'n'

firstNum, secondNum, nthNum = 0, 1, 0 #establish variables

if(n == 1):#if user wants n = 1
    print("The Fibonacci number for n = " + str(n) + " is 1")

else:#otherwise
    for currentN in range(n - 1):
        nthNum = firstNum + secondNum
        firstNum = secondNum
        secondNum = nthNum
    print("The Fibonacci number for n = " + str(n) + " is " + str(nthNum))