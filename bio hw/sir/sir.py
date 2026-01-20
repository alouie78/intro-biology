import random
import matplotlib.pyplot as pyplot

## Provided functions

def startingPop(popSize):
    '''Create a starting population, popSize large, where one individual
is infected, and the rest are susceptible.
    '''
    popL = 10*['I'] + (popSize-10)*['S']
    random.shuffle(popL)
    return popL

def plotOutbreak(infectedCountL):
    '''Convenience function for plotting an outbreak.'''
    pyplot.plot(range(len(infectedCountL)), infectedCountL)
    pyplot.xlabel('Days')
    pyplot.ylabel('Number of infections')
    pyplot.show()
    
##
def SIR(popL, probOfRecovery, numberOfContacts, probOfInfection):
    for i in range(len(popL)):
        if popL[i] == 'S':
            contacts = random.sample(popL, numberOfContacts)
            for contact in contacts:
                if contact == 'I':
                    chance = random.random()
                    if chance < probOfInfection:
                        popL[i] = 'E'
                        break

        elif popL[i] == 'I':
            chance = random.random()
            if chance < probOfRecovery:
                popL[i] = 'R'

    for i in range(len(popL)):
        if popL[i] == 'E':
            popL[i] = 'I'

    return popL

def outbreak(popSize,numDays,probOfRecovery,numberOfContacts,probOfInfection):
    popL = startingPop(popSize)
    infectedCountL = []
    for i in range(numDays):
        infected = 0
        popL = SIR(popL, probOfRecovery, numberOfContacts, probOfInfection)
        for j in range(len(popL)):
            if popL[j] == 'I':
                infected = infected + 1
        infectedCountL.append(infected)

    return (infectedCountL, popL)