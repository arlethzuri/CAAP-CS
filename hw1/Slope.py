#A program that returns the sum of digits given by the user

amountONums = eval(input("How many numbers would you like to add? ")) #ask number of digits to add
total = 0 #make accumulating var

for num in range(amountONums):
    total += eval(input("Enter a number: ")) #ask for the numbers
    
print("The sum is: " + str(total)) #return total sum