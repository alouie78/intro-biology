from hivSeqs import *
from distHelper import *
import math

def jukes(propDiff):
    """Correction for multiple hits using Jukes-Cantor model."""
    if propDiff < 0:
        print("jukes was passed a negative number, which it doesn't know how to handle.")
        return
    elif propDiff == 0:
        return 0
    elif propDiff < 0.75:
        return -3.0*math.log(1-(4.0*propDiff/3))/4
    else:
        print("jukes was passed a number >= 0.75, which is too big.")
        return

def propDifferent(seqA, seqB):
    diff = 0
    sites = 0
    for i in range(len(seqA)):
        if seqA[i] != seqB[i]:
            if seqA[i] != '-' and seqB[i] != '-':
                diff = diff + 1
                #print(diff)
    
    for i in range(len(seqA)):
        if seqA[i] != '-' and seqB[i] != '-':
            sites = sites + 1
            #print(sites)
    
    return diff/sites

def distances(strainNamesL, seqsL):
    D = {}
    for i in range(len(seqsL)):
        for j in range(len(seqsL)):
            pair = (strainNamesL[i], strainNamesL[j])
            D[pair] = jukes(propDifferent(seqsL[i], seqsL[j]))

    return D