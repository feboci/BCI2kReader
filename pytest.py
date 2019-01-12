import unittest
from BCI2kReader import BCI2kReader as b2k
import numpy as np
import os

########################################
## eeg1_1.dat, eeg1_2.dat : 64 Channels with 19696 samples, 8 states, 85 parameter fields
## 

class TestStartup(unittest.TestCase):
    def test_SimpleFileLoading(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'TestData/eeg1_1.dat')
        file=b2k.BCI2kReader(filename)
        self.assertNotEqual(file,None)
        file.close()

    def test_ReadInPlace(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'TestData/eeg1_1.dat')
        with b2k.BCI2kReader(filename,False) as file:
            signals, states = file.read(100)
            self.assertEqual(signals.shape,(64,100))
            self.assertEqual(states['Running'].shape,(1,100))
            
    def SliceNotationTest1(self, file):
        demo_slice=np.zeros((1,300))
        signals, states = file[5:99]
        self.assertEqual(signals.shape,(64,demo_slice[:,5:99].shape[1]),'Signals shape')
        self.assertEqual(states['Running'].shape,demo_slice[:,5:99].shape,'State shape')

    def SliceNotationTest2(self, file):
        demo_slice=np.zeros((1,300))
        signals, states = file[100:200:2]
        self.assertEqual(signals.shape,(64,demo_slice[:,100:200:2].shape[1]),'Signals shape with other stepsize')
        self.assertEqual(states['Running'].shape,demo_slice[:,100:200:2].shape,'State shape with other stepsize')

    def SliceNotationTest3(self,file):
        signals, states = file[19696-100:]
        self.assertEqual(signals.shape,(64,100),"Signals shape is not expected")
        self.assertEqual(states['Running'].shape,(1,100),'Signals shape is not expected')

    def SliceNotationTest4(self,file):
        signals, states = file[:99]
        demo_slice=np.zeros((1,300))
        self.assertEqual(signals.shape,(64,demo_slice[:,:99].shape[1]),'Signals shape')
        self.assertEqual(states['Running'].shape,demo_slice[:,:99].shape,'State shape')

    def SliceNotationTest5(self,file):
        signals, states = file[100]
        self.assertEqual(signals.shape,(64,1),'Signals shape')
        self.assertEqual(states['Running'].shape,(1,1),'State shape')

    def SliceNotationTest6(self,file):
        signals, states = file[-100]
        self.assertEqual(signals.shape,(64,1),'Signals shape')
        self.assertEqual(states['Running'].shape,(1,1),'State shape')

    def test_SliceInPlace1(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'TestData/eeg1_1.dat')
        with b2k.BCI2kReader(filename,False) as file:
            self.SliceNotationTest1(file)
            self.SliceNotationTest2(file)
            self.SliceNotationTest3(file)
            self.SliceNotationTest4(file)
            self.SliceNotationTest5(file)
            self.SliceNotationTest6(file)

    def test_SliceBuffered1(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'TestData/eeg1_1.dat')
        with b2k.BCI2kReader(filename,True) as file:
            file.signals # fills buffer
            self.SliceNotationTest1( file)
            self.SliceNotationTest2( file)
            self.SliceNotationTest3(file)
            self.SliceNotationTest4(file)
            self.SliceNotationTest5(file)
            self.SliceNotationTest6(file)


    def test_SignalSize(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'TestData/eeg1_1.dat')
        with b2k.BCI2kReader(filename) as file:
            print(file.signals.shape)
            self.assertEqual(file.signals.shape,(64,19696),'Signals shape is not expected')

if __name__ == "__main__":
	unittest.main()
