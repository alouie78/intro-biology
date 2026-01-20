from hiv1Mgroup import *

exTree=('anc', ('anc', (2007, (), (), 7.0), (1993, (), (), 3.0), 2.0), (1999, (), (), 7.0), 0)

exTree2=('anc',('anc',('anc',(2010,(),(),.01),(2007,(),(),.015),.02),(1994,(),(),.01),.01),('anc',('anc',(2001,(),(),.01),('anc',(2006,(),(),.02),(2004,(),(),.015),.01),.01),(2006,(),(),.03),.03),0)

def writeData(tree,fileName):
    '''Call extractData to get collection times and branch lengths, then
write these to file in tab-delimited form.'''
    L=extractData(tree)
    f=open(fileName,"w")
    for ct,br in L:
        f.write(str(ct)+"\t"+str(br)+"\n")
    f.close()


def extractData(tree): 
    tree = list(tree)

    if tree[1] == ():
        return [[tree[0], tree[3]]]
    else:
        left = extractData(tree[1])
        right = extractData(tree[2])
        length = left + right

        for item in range(len(length)):
            length[item][1] += tree[3]

        return length




