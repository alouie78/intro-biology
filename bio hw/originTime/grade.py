import unittest
import branchLen as hw


class SimpleTests(unittest.TestCase):

    def testB(self):
        exTree=('anc', ('anc', (2007, (), (), 7.0), (1993, (), (), 3.0), 2.0), (1999, (), (), 7.0), 0)
        self.assertTrue(compAns(hw.extractData(exTree),[[1993, 5.0], [1999, 7.0], [2007, 9.0]]),msg="problem in extractData")

        
    def testC(self):
        exTree2=('anc', ('anc', ('anc', (2010, (), (), 0.01), (2007, (), (), 0.015), 0.02), (1994, (), (), 0.01), 0.01), ('anc', ('anc', (2001, (), (), 0.01), ('anc', (2006, (), (), 0.02), (2004, (), (), 0.015), 0.01), 0.01), (2006, (), (), 0.03), 0.03), 0)
        self.assertTrue(compAns(hw.extractData(exTree2),[[2010, 0.04], [2007, 0.045000000000000005], [1994, 0.02], [2001, 0.05], [2006, 0.07], [2004, 0.065], [2006, 0.06]]),msg="problem in extractData")
    
    def testD(self):
        t=('anc', ('anc', (7, (), (), 0.5878285372378467), ('anc', (76, (), (), 0.5621617328178866), ('anc', (72, (), (), 0.26899353500033196), ('anc', (4, (), (), 0.2594633685327733), (33, (), (), 0.32770311509309413), 0.45365796986497653), 0.9787170239073663), 0.8367986882249194), 0.8789604045991225), (88, (), (), 0.996496340900122), 0)
        self.assertTrue(compAns(hw.extractData(t),[[7, 1.466788941836969], [76, 2.2779208256419285], [72, 2.96346965173174], [4, 3.407597455129158], [33, 3.4758372016894787], [88, 0.996496340900122]]),msg="problem in extractData")
    
    def testE(self):
        t=('anc', ('anc', ('anc', (44, (), (), 0.3418887419525336), (60, (), (), 0.5281663699751938), 0.9788299154798091), (92, (), (), 0.35812199576660686), 0.4962010677705623), ('anc', (9, (), (), 0.5846463816103634), (12, (), (), 0.8482340914830255), 0.7134991870253687), 0)
        self.assertTrue(compAns(hw.extractData(t),[[44, 1.8169197252029048], [60, 2.0031973532255654], [92, 0.8543230635371691], [9, 1.2981455686357322], [12, 1.5617332785083944]]),msg="problem in extractData")

    def testG(self):
        t=('anc', ('anc', (87, (), (), 0.9471395665837631), (74, (), (), 0.4879611723594022), 0.28606131126069334), (46, (), (), 0.02679747932992682), 0)
        self.assertTrue(compAns(hw.extractData(t),[[87, 1.2332008778444563], [74, 0.7740224836200955], [46, 0.02679747932992682]]),msg="problem in extractData")


def compAns(hwsol,sol):
    hwsol.sort()
    sol.sort()
    if len(hwsol) != len(sol): return False
    for i in range(len(sol)):
        if hwsol[i][0] != sol[i][0]: return False
        if round(hwsol[i][1],3) != round(sol[i][1],3): return False
    return True

if __name__ == '__main__':
    unittest.main()
