import unittest
import os
import numpy as np
from .helpers_for_test import MyDir, reading_test 
import weio

class Test(unittest.TestCase):
 
    def test_001_read_all(self):
        reading_test('HAWC*.*', weio.read)

    def DF(self,FN):
        """ Reads a file with weio and return a dataframe """ 
        return weio.read(os.path.join(MyDir,FN)).toDataFrame()

    def test_HAWC2(self):
        F=weio.read(os.path.join(MyDir,'HAWC2_out_ascii.dat'))
        DF=F.toDataFrame()
        self.assertEqual(DF.values[-1,1],-1.72572E+03)
        self.assertEqual(DF.values[-1,-1], 3.63349E+03)
        self.assertEqual(DF.columns[0], 'Time_[s]')
        self.assertEqual(DF.columns[1], 'WSP gl. coo.,Vy_[m/s]')

        # Test that "exported dat files" are the same
        # NOTE: cannot do comparison of sel files since names are different
        F.test_ascii(bCompareWritesOnly=True,bDelete=True)
        os.remove(os.path.join(MyDir,'HAWC2_out_ascii_TMP.sel'))
        os.remove(os.path.join(MyDir,'HAWC2_out_ascii_TMP2.sel'))

    def test_BHAWC(self):
        F=weio.read(os.path.join(MyDir,'BHAWC_out_ascii.sel'))
        DF=F.toDataFrame()
        self.assertEqual(DF.values[-1,1], 147.85)
        self.assertEqual(DF.columns[0], 't_[s]')
        self.assertEqual(DF.columns[1], 'ang_azi_[deg]')

        # Testing that "exported" sel files are the same
        F.test_ascii(bCompareWritesOnly=True,bDelete=True)
        os.remove(os.path.join(MyDir,'BHAWC_out_ascii_TMP.dat'))
        os.remove(os.path.join(MyDir,'BHAWC_out_ascii_TMP2.dat'))

        # Testing that "exported" dat files are the same
        F=weio.read(os.path.join(MyDir,'BHAWC_out_ascii.dat'))
        F.test_ascii(bCompareWritesOnly=True,bDelete=True)
        os.remove(os.path.join(MyDir,'BHAWC_out_ascii_TMP.sel'))
        os.remove(os.path.join(MyDir,'BHAWC_out_ascii_TMP2.sel'))

    def test_HAWCStab2(self):
        # power file
        F=weio.read(os.path.join(MyDir,'HAWCStab2.pwr'))
        DF=F.toDataFrame()
        self.assertAlmostEqual(DF.values[-1,1],0.1553480512E+05)
        self.assertAlmostEqual(DF.values[-1,-1], 0.3181950053E+09)
        self.assertEqual(DF.columns[0], 'V_[m/s]')
        self.assertEqual(DF.columns[1], 'P_[kW]')
        # induction files
        F=weio.read(os.path.join(MyDir,'HAWCStab2_u3000.ind'))  # normal .ind
        DF=F.toDataFrame()
        self.assertAlmostEqual(DF.values[-1,1],0.517961E+00)
        self.assertAlmostEqual(DF.values[-1,-1], 0.354614E-02)
        self.assertEqual(DF.columns[0], 's_[m]')
        self.assertEqual(DF.columns[1], 'A_[-]')
        F=weio.read(os.path.join(MyDir,'HAWCStab2_defl_u3000.ind'))  # defl .ind
        DF=F.toDataFrame()
        self.assertAlmostEqual(DF.values[-1,1],19)
        self.assertAlmostEqual(DF.values[-1,-1], 0.242932E-05)
        self.assertEqual(DF.columns[0], 's_[m]')
        self.assertEqual(DF.columns[1], 'Element_no_[-]')
        F=weio.read(os.path.join(MyDir,'HAWCStab2_fext_u3000.ind'))  # fext .ind
        DF=F.toDataFrame()
        self.assertAlmostEqual(DF.values[-1,1],20)
        self.assertAlmostEqual(DF.values[-1,-1], -0.170519E+03)
        self.assertEqual(DF.columns[0], 's_[m]')
        self.assertEqual(DF.columns[1], 'Node_[-]')
