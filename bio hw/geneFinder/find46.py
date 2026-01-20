import math
from findHelper import *

def find46():
    """Given coding and noncoding training data from E. coli, build a
    first order Markov model on codons and make predictions for
    sequences in Vibrio.
    """
    # load sequences
    ecoliCodeOrfL=[s.rstrip() for s in open("ecoliCodeTrainOrfs-mid.txt","r").readlines()]
    ecoliNoncodeOrfL=[s.rstrip() for s in open("ecoliNcTrainOrfs-mid.txt","r").readlines()]
    vibAllOrfL=[s.rstrip() for s in open("vibAllOrfs-mid.txt","r").readlines()]
    # run model
    ecoliCodeProbD=condProb(ecoliCodeOrfL)
    ecoliNoncodeProbD=condProb(ecoliNoncodeOrfL)
    llrD=makeLogLikelihoodRatioD(ecoliCodeProbD,ecoliNoncodeProbD)
    vibCodePredL,vibNoncodePredL=predict(vibAllOrfL,llrD)

    return vibCodePredL,vibNoncodePredL

def makeLogLikelihoodRatioD(codeProbD,noncodeProbD):
    """Make a dictionary of log likelihood ratios from coding and
    noncoding Markov models."""
    llrD={}
    for key in codeProbD:
        llrD[key] = math.log( codeProbD[key]/noncodeProbD[key] )
    return llrD

def logLikelihoodRatioSum(orf, llrD):
    sum = 0
    i = 0
    while i < len(orf) - 5:
        if i == len(orf) - 5:
            twoCodon = orf[i:]
        else:
            twoCodon = orf[i:i+6]

        sum = sum + llrD[twoCodon]
        i = i + 3

    return sum

def count(orfL):
    codonCountD,twoCodonCountD=initializeCountDicts()
    for seq in orfL:
        i = 0
        while i < len(seq) - 5:
            if i == len(seq) - 5:
                codon = seq[i:i+3]
                twoCodon = seq[i:]
            else:
                codon = seq[i:i+3]
                twoCodon = seq[i:i+6]

            codonCountD[codon] = codonCountD[codon] + 1
            twoCodonCountD[twoCodon] = twoCodonCountD[twoCodon] + 1

            i = i + 3

    return codonCountD,twoCodonCountD

def condProb(orfL):
    codonCountD,twoCodonCountD = count(orfL)
    for key in twoCodonCountD:
        twoCodonCountD[key] = twoCodonCountD[key] / codonCountD[key[:3]]

    return twoCodonCountD

def predict(orfL, llrD):
    codingL = []
    noncodingL = []

    for orf in orfL:
        likelihood = logLikelihoodRatioSum(orf, llrD)
        if likelihood > 0:
            codingL.append(orf)
        if likelihood < 0:
            noncodingL.append(orf)

    return codingL, noncodingL