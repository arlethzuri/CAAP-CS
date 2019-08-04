# Arleth Salinas
# Lab 4
# August 4, 2019; 10pm

# Imports the turtle graphics module
import turtle
 
# creates a turtle (pen) an sets the speed (where 0 is fastest and 10 is slowest)
# The colors can be set through their names or through hexadecimal codes, use hex for accuracy
startingX = -200
startingY = 200
turtle.screensize(200, 200, bg="#FFFFFF")
turtle.tracer(60)
myPen = turtle.Turtle()
myPen.color("#000000")
myPen.speed(0)
doneDrawing = False

# If you would like to slow down the animation, uncomment the next line. Higher delay, the slower it will be
#turtle.delay(100)

# setting out box sizes to the n sq pixels per box
boxSize = 10
 
#paths of each art piece
choices = ['art/banana.txt', 'art/blinky.txt', 'art/epic_smiley_face.txt', 'art/mario.txt', 'art/mushroom.txt', 'art/heart.txt', 'art/sushi.txt']
#names of each art piece
choiceNames = ['banana', 'blinky', 'epic smiley face', 'mario', 'mushroom', 'heart', 'sushi']

# myPen.setheading(n) points pen to given angle direction.
# where n equeals the angle (think unit circle).
# 0 points to the right, 90 to go up, 180 to go to the left 270 to go down

# Positions myPen in top left area of the screen
# This canvas is currently set to 200*200 pixels or a 20x20 box of 10 sq pixels each
def goto_origin():
    myPen.penup()
    myPen.setposition(startingX, startingY)
    myPen.pendown()

def move_pen(x, y):
    myPen.penup()
    myPen.setposition(x, y)
    myPen.pendown()

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    # Can also be done with a for loop - Can you rewrite thise function as such?
    myPen.begin_fill()

    for i in range(4):
        myPen.forward(intDim)
        myPen.left(90)

    myPen.end_fill() 

# Here is an example of how to draw a box using the box function      
# Comment these two lines out when you draw your own images
#box(boxSize)
#turtle.done()

# Challenge functions (2 bonus pts each) 
#cite: https://stackoverflow.com/questions/4071633/python-turtle-module-saving-an-image
def save_image(): # saves the screen to an image/vector file
    temp = myPen.getscreen()
    temp.getcanvas().postscript(file="myImage.eps")

# You have a function for boxes, can you make functions for circles and triangles?
#def circle(intRadius):
    
def triangle(intLength, color): #This can be an equilateral triangle, or not
    myPen.begin_fill()
    myPen.color(color)
    
    for i in range(2):
        myPen.forward(intLength)
        myPen.left(60)
        
    myPen.end_fill()
    turtle.done()
    
# These are the instructions on how to move "myPen" around after drawing a box.
# penup() lifts the pen so it doesn't draw anything and can be moved freely
# pendown() puts the pen down and it draws as it moves, e.g.:
# myPen.penup()
# myPen.forward(boxSize)
# myPen.pendown()
 
# You will save your drawings in text files, which you will read from the art folder.
# You have two sample art pieces already saved. The first line will be a list of colors, and the 
# rest of the lines will be rows of pixels, which you should read and save as a list of lists.
# This first list stores the color values, e.g.:
# #FFFFFF,#FFFF00,#000000,#61380B,#F4FA58
# The drawings are stored using a "list of lists" structure where each value within every list
# element is the index of the color in the pallet list for that pixel

# This function will take in a filename path and load the art piece stored in that file.
# You are to parse the art into two lists, one for the color palette (first line of file),
# and a second with the pixel values (list of lists).
# The function returns both lists
def load_art(path):    
    #first open the file and store all lines into 'lines'
    artFile = open(path, "r")
    lines = artFile.read().splitlines()#using splitlines removes '\n' when using split later on
    
    #store the first line into tempPallet, then split list
    #into each color and store into myPallet
    tempPallet = lines[0]
    myPallet = tempPallet.split(",")
    
    #make an empty list and assign to 'myPixels'
    myPixels = list()
    
    #in each line, excluding the first line, split by comma and store that
    #list into myPixels
    for i in range(1, len(lines)):
        tempList = lines[i].split(",")
        myPixels.append(tempList)
    
    return myPallet, myPixels
    
# This function takes a pallet and pixel list (matrix) to draw the picture
# You are to write this function
def draw(pallet, pixels):
    goto_origin()
    currentY = startingY
    for i in range(len(pixels)):
        for j in pixels[i]:
            myPen.color(pallet[int(j)])
            myPen.begin_fill()
            box(boxSize)
            myPen.end_fill()
            myPen.forward(boxSize)
        currentY -= 10
        move_pen(startingX, currentY)

#ask user what they want to draw
def ask_user():
    #ask user which drawing they'd like to see
    print("What drawing would you like to see?")
    #print out each choice
    for i in range(len(choiceNames)):
        print((i + 1), choiceNames[i])    
    #user input
    userChoice = eval(input(">> "))
    return userChoice
            
# Should give the user a list of the possible drawing pieces you have and ask which one to draw
# After drawing the piece, ask them if they would like to draw a different piece until they quit the program.
if __name__ == '__main__':    
    while not doneDrawing:
        #ask user for which drawing
        userChoice = ask_user()

        #sample for loading art and calling draw
        pallet_1, pixels_1 = load_art(choices[userChoice - 1])

        #draw the piece of art
        draw(pallet_1, pixels_1)
        
        #ask user if they want to draw something new
        print("Would you like to draw something new?")
        
        print("1 Yes\n2 No")
        
        userResponse = eval(input(">> "))
        
        #if user wants to draw another piece of art
        if(userResponse == 1):
            doneDrawing = False
            turtle.clearscreen() #empty screen and reset pen to origin
            move_pen(startingX, startingY)#move pen to upper left corner
            turtle.tracer(50) #set tracer speed
        else: #otherwise
            doneDrawing = True #end while loop by setting 'doneDrawing' to true