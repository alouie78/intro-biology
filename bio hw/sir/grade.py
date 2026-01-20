import unittest
import sir as hw


class SimpleTests(unittest.TestCase):

    def testB(self):
        # SIR
        popL = 800*['S'] + 100*['R']+100*['I']
        newPopL = hw.SIR(popL,.1,10,.1)
        self.assertTrue(len(newPopL)==1000,msg="problem in SIR, population size changes")
        self.assertTrue(newPopL.count('R')>= 100,msg="problem in SIR, number of R must stay same or increase")
        self.assertTrue(newPopL.count('S')<= 800,msg="problem in SIR, number of S must stay same or decrease")
        
    def testC(self):
        # SIR
        popL = 100*['S'] + 50*['R']+90*['I']
        newPopL = hw.SIR(popL,.1,10,.1)
        self.assertTrue(len(newPopL)==240,msg="problem in SIR, population size changes")
        self.assertTrue(newPopL.count('R')>= 50,msg="problem in SIR, number of R must stay same or increase")
        self.assertTrue(newPopL.count('S')<= 100,msg="problem in SIR, number of S must stay same or decrease")
        

    def testD(self):
        # SIR
        popL = 900*['S'] + 100*['I']
        newPopL = hw.SIR(popL,1.0,10,1)
        self.assertTrue(newPopL.count('R')==100,msg="problem in SIR")
        self.assertTrue(newPopL.count('I')>530,msg="problem in SIR")
        self.assertTrue(newPopL.count('I')<660,msg="problem in SIR")
        
    def testE(self):
        # outbreak
        InfectedCountL,PopulationL = hw.outbreak(500,150,.1,50,1)

        self.assertTrue(PopulationL.count('R') == 500,msg="problem in outbreak")
        mx = max(InfectedCountL)
        mxind = InfectedCountL.index(mx)
        self.assertTrue(mx > 400,msg="problem in outbreak")
        self.assertTrue(mxind < 5,msg="problem in outbreak")
        
if __name__ == '__main__':
    unittest.main()
