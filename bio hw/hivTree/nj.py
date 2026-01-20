from hivDist import *
from njHelper import *

def nodeSep(node,nodeL,distD):
    '''A measure of the separation between a node of interest and
    the other nodes.'''
    distSum=0
    for iternode in nodeL:
        if node != iternode:
            distSum+=distD[(node,iternode)]
    return(float(distSum)/(len(nodeL)-2))

def njMetric(node1,node2,nodeL,distD):
    '''Calculates the neighbor joining metric between two nodes.'''
    d=distD[(node1,node2)]
    s1=nodeSep(node1,nodeL,distD)
    s2=nodeSep(node2,nodeL,distD)
    return(d-s1-s2)

def branchLength(nodeA,nodeB,nodeL,distD):
    '''Takes two nodes we're planning to merge, nodeA and nodeB. Calculates the
branch lengths from their common ancestor to each.'''
    dist=distD[(nodeA,nodeB)]
    sepA=nodeSep(nodeA,nodeL,distD)
    sepB=nodeSep(nodeB,nodeL,distD)
    branchA=0.5*(dist+(sepA-sepB))
    branchB=0.5*(dist+(sepB-sepA))
    return(branchA,branchB)

def bestPair(nodeL, distD):
    bestI = nodeL[0]
    bestJ = nodeL[0]
    bestDistance = 2147483647
    for i in range(len(nodeL)):
        for j in range(i+1, len(nodeL)):
            d = njMetric(nodeL[i], nodeL[j], nodeL, distD)
            if bestDistance > d:
                bestDistance = d
                bestI = nodeL[i]
                bestJ = nodeL[j]

    return (bestI, bestJ)

def mergeNodes(nodeA,nodeB,branchLenA,branchLenB):
    newA = (nodeA[0], nodeA[1], nodeA[2], branchLenA)
    newB = (nodeB[0], nodeB[1], nodeB[2], branchLenB)
    return ('anc', newA, newB, 0)

def updateDistances(nodeA,nodeB,newNode,nodeL,distD):
    for i in nodeL:
        if i != nodeA and i != nodeB:
            x = (distD[(i, nodeA)] + distD[(i, nodeB)] - distD[(nodeA, nodeB)])
            newDist = 0.5 * x
            if distD != 0:
                distD[(newNode, i)] = newDist
                distD[(i, newNode)] = newDist

def nj(nodeL, distD):
    while len(nodeL) > 2:
        nodeA, nodeB = bestPair(nodeL, distD)
        #print('nodeA = ', nodeA, 'nodeB =', nodeB)
        branchLengthA, branchLengthB = branchLength(nodeA, nodeB, nodeL, distD)
        newNode = mergeNodes(nodeA, nodeB, branchLengthA, branchLengthB)
        #print('newNode = ', newNode)
        updateDistances(nodeA, nodeB, newNode, nodeL, distD)
        nodeL.remove(nodeA)
        #print('remove nodeA =', nodeL)
        nodeL.remove(nodeB)
        #print('remove nodeB =', nodeL)
        nodeL.append(newNode)
        #print('add newNode =', nodeL)

    return terminate(nodeL, distD)
    
def terminate(nodeL, distD):
    dist = distD[(nodeL[0], nodeL[1])]
    dist = dist/2
    nodeA = (nodeL[0][0], nodeL[0][1], nodeL[0][2], dist)
    nodeB = (nodeL[1][0], nodeL[1][1], nodeL[1][2], dist)
    return ('anc', nodeA, nodeB, 0)