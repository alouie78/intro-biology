import matplotlib.pyplot as pyplot
from scipy import stats
import numpy

def plotTimes(fileName):
    '''Given a tab-delimited file of collection times and branch lengths,
make a plot with regression line.'''
    f=open(fileName,'r')
    cTimeL=[]
    brL=[]
    while True:
        s=f.readline()
        if s=='':
            break
        ct,br=s.split('\t')
        cTimeL.append(int(ct))
        brL.append(float(br))

    pyplot.plot(cTimeL,brL,'o')
    pyplot.axis([1850,2020,0,.35])

    slope, intercept, r_value, p_value, slope_std_error = stats.linregress(cTimeL,brL)

    # plot best fit line
    x=numpy.array([1850,2020])
    y=x*slope+intercept
    pyplot.plot(x,y,'r')
    pyplot.show()
