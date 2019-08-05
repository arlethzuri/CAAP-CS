import main
import turtle

#this tests the rewritten box function, it works
#main.box(50)

#this tests to see if the proper lists are stored in the 'load_art' function in main
listOne, listTwo = main.load_art('art/banana.txt')

print("List one is the colors: ")
colors = ""

for i in listOne:
    print(i)

print("List two is the pixel order: ")
for j in listTwo:
    print(j)
    
#this tests out the 'draw' function, works
main.draw(listOne, listTwo)

#this tests out the 'save_image' function
main.save_image()

#this tests out the 'triangle'
main.triangle(50, "#000000")

#this tests my circle function
main.circle(10, "#000000")