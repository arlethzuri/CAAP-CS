#This program determines how many coins must be given in order to return the sufficient amount of change to the user

changeWanted = eval(input("Input change owed: ")) #ask for the amount of change wanted

coinVals = [.01, .05, .10, .25] #set values of coins

coinsReturned = 0 #variable to count coins to return

currentCoin = 3 #start at index 3 of coinVals

while currentCoin >= 0: #while all coin options have not yet been exhausted
    if round(changeWanted, 2) - coinVals[currentCoin] < 0: #if the change wanted minus the current coin is negative
        currentCoin -= 1 #move index to the next coin, of lesser value
    else: #otherwise, if change wanted minus the current coin isn't negative
        coinsReturned += 1 #add to count of coins returned
        changeWanted -= coinVals[currentCoin] #find new value of change wanted
        
print("Coins returned is " + str(coinsReturned)) #output number of coins returned