#A program that converts from Fahrenheit to Celsius and... prints the value 5 times.

initVal = eval(input("Go ahead and enter a Fahrenheit value to convert to Celsius: ")) #store initial F value

print("The temperature in Celsius is...")

for prints in range(5): #print result 5 times
    print((initVal - 32)*(5/9))