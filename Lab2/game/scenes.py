# imports random madule form library
import random

# the base class for the scenes. 
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene(). 
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.

difficulty = 0 #a variable to store which difficulty the user chooses
correctChoice = 0 #a variable to store which choice is the current 'correct' choice, so the next scene knows which text to display

class Scene(object):

    def enter(self):
        print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
        print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
        exit(1)


class Difficulty(Scene):
    name = 'difficulty'

    def enter(self):
        print("Select a difficulty")
        print("1.) Easy, each scene has one consistent correct choice.")
        print("2.) Medium, each scene has one random correct choice between 2 choices")
        print("3.) Difficult, each scene has one random correct choice between all 3 choices")
        return self.action()

    def action(self):
        global difficulty
        choice = input("\n> ")

        if choice == ':q':
            return self.exit_scene(choice)
        # this is some exception handling, you don't need to worry about it, 
        # just accept that it works and keeps the program from falling apart.
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            return self.exit_scene(self.name)


        if int(choice) == 1:
            difficulty = 1
            return self.exit_scene('downtown_chicago')
        elif int(choice) == 2:
            difficulty = 2
            return self.exit_scene('downtown_chicago')
        elif int(choice) == 3:
            difficulty = 3
            return self.exit_scene('downtown_chicago')
        else:
            print("Ummmm.... please input an actual choice... ")
            return self.exit_scene(self.name)

    def exit_scene(self, outcome):
        return outcome

class DowntownChicago(Scene):#this scene doesn't have the possiblity of death lol
    name = 'downtown_chicago'

    def enter(self):
        print("It's 7pm and you just said goodbye to some friends after spending the night out in Chicago.")
        return self.action()

    def action(self):
        print("What were you guys up to?")
        print("1.) We had a fine dinner")
        print("2.) We went clubbing")
        print("3.) We went shopping.")
        choice = input("> ")

        if choice == ':q':
            return self.exit_scene(choice)
        # this is some exception handling, you don't need to worry about it, 
        # just accept that it works and keeps the program from falling apart.
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            return self.exit_scene(self.name)


        if int(choice) == 1:
            print("Ohh, fancy.")
            return self.exit_scene('red_line')
        elif int(choice) == 2:
            print("Hmm, interesting.")
            return self.exit_scene('red_line')
        elif int(choice) == 3:
            print("That sounds fun!")
            return self.exit_scene('red_line')
        else:
            print("Ummmm.... please input an actual choice... ")
            return self.exit_scene(self.name)

    def exit_scene(self, outcome):
        return outcome

class RedLine(Scene):
    name = 'red_line'

    #This is a list of possible outcomes based on user input, used for difficulties 2 & 3
    wrongChoices = ["You confront the man and demand why he keeps staring at you. He glares at you, pulls out a pocket knife, and slits your throat. Yikes...", "You keep waiting and hope the train arrives soon. A few moments later you hear the train coming and relieved get ready to get on. Suddenly though, you feel a strong shove and fall down into the rails. You don't get electrecuted, but you do get run over by the train...", "You decide to be friendly and greet the man, to try to relieve the tension. You turn around and wave. The man frowns at you and pulls a gun on you. BAM. As you bleed out, the man pick pockets you and runs away."]
    
    def enter(self):
        print("You're not too far from the red line, so you make your way to the station on foot. You make it to the station and wait by the edge. You notice though that a man in your peripheral vision is facing you. He seems to be staring at you. You're beginning to get a little uncomfortable.")
        return self.action()

    def action(self):
        global correctChoice
        print("What do you do?")
        print("1.) Confront him.")
        print("2.) Ignore him.")
        print("3.) Greet him.")
        choice = input("> ")

        if choice == ':q':
            return self.exit_scene(choice)
        # this is some exception handling, you don't need to worry about it, 
        # just accept that it works and keeps the program from falling apart.
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            return self.exit_scene(self.name)


        if(difficulty == 1): #only once choice is correct, it is always choice 3
            correctChoice = 3
            if int(choice) == 1:
                print(self.wrongChoices[0])
                return self.exit_scene('death')
            elif int(choice) == 2:
                print(self.wrongChoices[1])
                return self.exit_scene('death')
            elif int(choice) == 3:
                print("Good choice.")
                return self.exit_scene('train_car')
            else:
                print("Ummmm.... please input an actual choice... ")
                return self.exit_scene(self.name)
        elif(difficulty == 2):
            goodChoice = random.randint(1, 3) #choose a random choice of the first two as the good one
            correctChoice = goodChoice #save this random choice in global variable for next scene to refer to
            print("Correct choice is: ", correctChoice)
            if int(choice) == goodChoice: #if user inputs correct choice
                print("Good choice.")
                return self.exit_scene('train_car')
            elif(choice != 1 and choice != 2 and choice != 3):
                print("Ummmm.... please input an actual choice... ")
                return self.exit_scene(self.name)
            else:#otherwise
                print(self.wrongChoices[choice - 1])
                return self.exit_scene('death')
        elif(difficulty == 3): 
            goodChoice = random.randint(1, 4) #choose a random choice of all three as the good one
            correctChoice = goodChoice #save this random choice in global variable for next scene to refer to
            print("Correct choice is: ", correctChoice)
            if int(choice) == goodChoice: #if user inputs correct choice
                print("Good choice.")
                return self.exit_scene('train_car')
            elif(choice != 1 and choice != 2 and choice != 3):
                print("Ummmm.... please input an actual choice... ")
                return self.exit_scene(self.name)
            else:
                print(self.wrongChoices[choice - 1])
                return self.exit_scene('death')
            
    def exit_scene(self, outcome):
        return outcome

class TrainCar(Scene):
    name = 'train_car'
    
    #This is a list of possible outcomes based on user input, used for difficulties 2 & 3    
    wrongChoices = ["You decide to take a nap, so you rest your head against the wall and doze off. In your unconciousness, a mugger gets on the train and tries to pick-pocket you. You awaken and try to resist, but the mugger pulls a knife and stabs you in the chest. He runs off the train and you bleed to death...", "The train reaches a stop and you decide to stand up. However, someone sits beside just as you stand up. The person begins to argue with you claiming you stood up because you didn't want to be beside them. You try to explain yourself, but the stranger is too enraged to listen. They pull a gun and shoot you in the chest.", "You blast music thru your headphones and watch out the window, trying to stay awake. You get so distracted staring out of the window, that you don't notice woman across from you asking you to turn your music down. She grows frustrated and walks up to you. You still fail to notice, and feeling fed up, the woman yanks your headphones out and you instinctivly slap her. With utter shock, she turns to her husband who pulls out a knife and attacks you. RIP."]
    
    #Depending on what choice is correct, as is stored in global variable 'correctChoice', one of these dialogues is used
    rightChoices = ["You confront the man and demand why he keeps staring at you. He seems startled and simply turns and walks away.... weird, but okay. The trains arrives, you get comfortable and as the train starts moving you realize how sleepy you begin to feel.", "You decide to keep ignoring the stranger and just hope the train arrives soon. A few moments later you hear the train coming and relieved you get on. You get comfortable and as the train starts moving you realize how sleepy you begin to feel.", "You and the stranger, whose name you learn is Dan, end up having a nice conversation while awaiting the train. He tells you about how his social anxiety makes him come off a bit strange and that he can have pretty bad anger issues. Best not to get on his bad side... You both hop onto the train and you find a nice spot all to yourself. You get comfortable and as the train starts moving you realize how sleepy you begin to feel."]
    
    def enter(self):
        print("**Checkpoint**")
        #because the global variable changes, if user dies and needs to replay scene, it may not replay
        #the correct one, so locally store the correct choice that plays here in 'checkScene' variable
        checkScene = correctChoice - 1
        print(self.rightChoices[checkScene])
        return self.action()

    def action(self):
        global correctChoice
        print("What do you do?")
        print("1.) Take a nap.")
        print("2.) Stand up instead of sit.")
        print("3.) Blast some music thru your headphones.")
        choice = input("> ")

        if choice == ':q':
            return self.exit_scene(choice)
        # this is some exception handling, you don't need to worry about it, 
        # just accept that it works and keeps the program from falling apart.
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            return self.exit_scene(self.name)


        if(difficulty == 1):#Choice 2 is correct each time
            correctChoice = 2
            if int(choice) == 1:
                print(self.wrongChoices[0])
                return self.exit_scene('death')
            elif int(choice) == 2:
                print("Nice choice.")
                return self.exit_scene('cross_walk')
            elif int(choice) == 3:
                print(self.wrongChoices[2])
                return self.exit_scene('death')
            else:
                print("Ummmm.... please input an actual choice... ")
                return self.exit_scene(self.name)

        elif(difficulty == 2):
            goodChoice = random.randint(1, 3)#Choose a random choice from the first two as good
            correctChoice = goodChoice
            
            if int(choice) == goodChoice:#if user inputs correct choice
                print("Good choice.")
                return self.exit_scene('cross_walk')
            elif(choice != 1 and choice != 2 and choice != 3):
                print("Ummmm.... please input an actual choice... ")
                return self.exit_scene(self.name)
            else: #otherwise
                print(self.wrongChoices[choice - 1])
                return self.exit_scene('death')
        elif(difficulty == 3):#Choose a random choice from all three as good
            goodChoice = random.randint(1, 4)
            correctChoice = goodChoice
            print("Correct choice is: ", correctChoice)
            if int(choice) == goodChoice:
                print("Good choice.")
                return self.exit_scene('cross_walk')
            elif(choice != 1 and choice != 2 and choice != 3):
                print("Ummmm.... please input an actual choice... ")
                return self.exit_scene(self.name)
            else:
                print(self.wrongChoices[choice - 1])
                return self.exit_scene('death')
            
    def exit_scene(self, outcome):
        return outcome

class CrossWalk(Scene):
    name = 'cross_walk'
    
    wrongChoices = ["In an attempt to get across the street, you decide to dash across. Unfortunately, you trip and land face first into the pavement. You're hard to see on the road, and as you groggily try to get up, a car runs straight across you.", "You decide to walk across the street even though you've only three seconds. You see cars coming, but surely they'll stop and wait right? ... No, they don't, and now you're roadkill.", "You wait instead of crossing. You sit by a pole and lean your head against it. Getting a bit comfortable, you fall asleep. You wake up to a group of men beating you to death and stealing your stuff."]
    
    rightChoices = ["You decide to take a nap. You set an alarm on your phone so you don't sleep past your stop. 30 minutes pass and your alarm wakes you. Your stop arrives shortly thereafter. You get off the train and head to your bus stop. You get ready to cross the street, but the walking signal only gives you 3 seconds to cross.", "Despite feeling a bit tired to stand, you do so anyways to avoid falling asleep. You finally make it to your stop at 8:30pm. You get off the train and head to your bus stop. You get ready to cross the street, but the walking signal only gives you 3 seconds to cross.", "You decide to blast music through your headphones so you don't fall asleep. No one seems to mind your music either. You get off the train and head to your bus stop. You get ready to cross the street, but the walking signal only gives you 3 seconds to cross."]
    
    def enter(self):
        print(self.rightChoices[correctChoice - 1])
        return self.action()

    def action(self):
        global correctChoice
        print("What do you do?")
        print("1.) Dash across the street.")
        print("2.) Walk across the street.")
        print("3.) Wait.")
        choice = input("> ")

        if choice == ':q':
            return self.exit_scene(choice)
        # this is some exception handling, you don't need to worry about it, 
        # just accept that it works and keeps the program from falling apart.
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            return self.exit_scene(self.name)


        if(difficulty == 1):
            correctChoice = 2
            if int(choice) == 1:
                print(self.wrongChoices[0])
                return self.exit_scene('death')
            elif int(choice) == 2:
                print("Good choice.")
                return self.exit_scene('broke_bus')
            elif int(choice) == 3:
                print(self.wrongChoices[2])
                return self.exit_scene('death')
            else:
                print("Ummmm.... please input an actual choice... ")
                return self.exit_scene(self.name)
        elif(difficulty == 2):
            goodChoice = random.randint(1, 3)
            correctChoice = goodChoice
            print("Correct choice is: ", correctChoice)
            if int(choice) == goodChoice:
                print("Good choice.")
                return self.exit_scene('broke_bus')
            elif(choice != 1 and choice != 2 and choice != 3):
                print("Ummmm.... please input an actual choice... ")
                return self.exit_scene(self.name)
            else:
                print(self.wrongChoices[choice - 1])
                return self.exit_scene('death')
        elif(difficulty == 3):
            goodChoice = random.randint(1, 4)
            correctChoice = goodChoice
            print("Correct choice is: ", correctChoice)
            if int(choice) == goodChoice:
                print("Good choice.")
                return self.exit_scene('broke_bus')
            elif(choice != 1 and choice != 2 and choice != 3):
                print("Ummmm.... please input an actual choice... ")
                return self.exit_scene(self.name)
            else:
                print(self.wrongChoices[choice - 1])
                return self.exit_scene('death')
            
    def exit_scene(self, outcome):
        return outcome

class BrokeBus(Scene):
    name = 'broke_bus'

    wrongChoices = ["You decide to order an uber and end up only waiting about 15 minutes before it arrives. Feeling drowsy and out of energy, you plop in. You ask the driver to let you know when you're home and to wake you up, if they'd be so kind. They agree to do so and you take a nap. The driver wakes you up, but you find yourself tied up in a chair in what appears to be a basement. You panic and realize you never actually checked the license plate of the car to assure that was the right car... you got into the wrong car and ended up being kidnapped. Your body is found weeks later.", "You begrugdingly decide to wait for the bus. You sit against a fence and rest your eyes. You end up drifting off to sleep, and sadly no one notices you and the bus that arrives leaves you behind. You awaken to a group of men beating you to death and stealing your stuff."]
    
    rightChoices = ["You decide to dash across the street! Cars speed across immediately after. Phew. You and a few others await the bus. It takes half an hour to arrive, but when it finally does, it breaks down. You're told that another bus will arrive to take passengers, however it'll likely take 45 minutes. You become frustrated, especially because it's already 9pm and you just want to get home and relax.", "You decide to walk across the street even though you've only three seconds. Luckily, the cars see you and wait for you to finish crossing. You and a few others await the bus. It takes half an hour to arrive, but when it finally does, it breaks down. You're told that another bus will arrive to take passengers, however it'll likely take 45 minutes. You become frustrated, especially because it's already 9pm and you just want to get home and relax.", "You decide just to wait until the signal tells you to move again. You sit by a pole and rest your head, feeling quite ready for bed... then the crossing signal changes and allows you to walk. You and a few others await the bus. It takes half an hour to arrive, but when it finally does, it breaks down. You're told that another bus will arrive to take passengers, however it'll likely take 45 minutes. You become frustrated, especially because it's already 9pm and you just want to get home and relax."]
    
    finalRightChoices = ["You decide to order an uber and end up only waiting about 15 minutes before it arrives. You hop in and head home.", "You begrugdingly decide to wait for the bus. You sit against a fence and rest your eyes. You end up drifting off to sleep. Luckily, a kind woman nudges you awake.\n'This is your bus too right?'\n You smile and sit with her on the bus. You learn her name is Mary and you both exchange numbers. Once at your stop, you say goodbye and finally head home."]
    
    def enter(self):
        print("**Checkpoint**")
        checkScene = correctChoice - 1
        print(self.rightChoices[checkScene])
        return self.action()

    def action(self):
        global correctChoice
        print("What do you do?")
        print("1.) Order an uber.")
        print("2.) Wait for the bus.")
        choice = input("> ")

        if choice == ':q':
            return self.exit_scene(choice)
        # this is some exception handling, you don't need to worry about it, 
        # just accept that it works and keeps the program from falling apart.
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            return self.exit_scene(self.name)


        if(difficulty == 1):
            correctChoice = 1
            if int(choice) == 1:
                print(self.finalRightChoices[0])
                return self.exit_scene('finished')
            elif int(choice) == 2:
                print(self.wrongChoices[1])
                return self.exit_scene('death')
            else:
                print("Ummmm.... please input an actual choice... ")
                return self.exit_scene(self.name)
        elif(difficulty == 2):
            goodChoice = random.randint(1, 3)
            correctChoice = goodChoice
            print("Correct choice is: ", correctChoice)
            if int(choice) == goodChoice:
                print("Good choice.")
                return self.exit_scene('finished')
            elif(choice != 1 and choice != 2 and choice != 3):
                print("Ummmm.... please input an actual choice... ")
                return self.exit_scene(self.name)
            else:
                print(self.wrongChoices[choice - 1])
                return self.exit_scene('death')
        elif(difficulty == 3):
            goodChoice = random.randint(1, 4)
            correctChoice = goodChoice
            print("Correct choice is: ", correctChoice)
            if int(choice) == goodChoice:
                print(finalRightChoices[choice - 1])
                return self.exit_scene('finished')
            elif(choice != 1 and choice != 2 and choice != 3):
                print("Ummmm.... please input an actual choice... ")
                return self.exit_scene(self.name)
            else:
                print(self.wrongChoices[choice - 1])
                return self.exit_scene('death')
            

    def exit_scene(self, outcome):
        return outcome