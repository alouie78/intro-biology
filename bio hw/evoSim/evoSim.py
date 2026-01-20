import random
from Org import *

def procreate(orgL, popSize, mutProb):
    newPop = []
    for i in range(popSize):
        org = random.choice(orgL)
        newOrg = org.replicate(mutProb)
        newPop.append(newOrg)

    return newPop

def evoSim(popL,popSize,numGen,mutProb):
    generations = []
    generations.append(popL)
    currentPop = popL
    while len(generations) < numGen + 1:
        currentPop = procreate(currentPop, popSize, mutProb)
        generations.append(currentPop)

    return generations

def evoSimSelect(popL,popSize,numGen,mutProb,fitnessD):
    generations = []
    generations.append(popL)
    currentPop = popL
    while len(generations) < numGen + 1:
        currentPop = procreate(currentPop, popSize, mutProb)
        generations.append(currentPop)
        currentPop = cullPop(currentPop, fitnessD)

    return generations