from choleraData import *

def printIslands(coordsL,geneInfoL,geneCoordL):
    """For each potential island in coordsL print location and gene
    info."""
    for coords in coordsL:
        print("** Island")
        print("  chrom",geneCoordL[coords[0]][1],)
        print(geneCoordL[coords[0]][2]+"-"+geneCoordL[coords[1]-1][3])
        # print genes from coords[0] to coords[1], not including coords[1]
        for i in range(coords[0],coords[1]):
            print("  "+geneInfoL[i])
        print()

def cholera():
    hasHomologL = hasHomolog(vcN16961_vs_vcPS15,vcN16961_vs_vc2740_80,700)
    coordsL = islands(hasHomologL,12)
    printIslands(coordsL,vcN16961geneInfoL,vcN16961geneCoordL)

def hasHomolog(mat1,mat2,threshold):
    result = []
    
    for i in range(len(mat1)):
        most1 = max(mat1[i])
        most2 = max(mat2[i])
        if most1 < threshold and most2 < threshold:
            result.append(0)
        else:
            result.append(1)
    
    return result

def islands(hasHomologL,minSize):
    result = []
    i = 0
    while i < len(hasHomologL):
        if hasHomologL[i] == 0:
            if i + minSize <= len(hasHomologL):
                homolog = True
                for j in range(minSize):
                    if hasHomologL[i+j] != 0:
                        homolog = False
                        break
                if homolog == True:
                    count = 0
                    for k in range(len(hasHomologL) - i):
                        if hasHomologL[i+k] == 0:
                            count = count + 1
                        else:
                            break
                    result.append((i, i+count))
                    i = i + count
                else:
                    i = i + 1
            else:
                i = i + 1
            
        else:
            i = i + 1

    result.sort(key=lambda t: t[0] - t[1])
    
    return result
