import unittest
from BCI2kReader import BCI2kReader as b2k
import os

class TestStartup(unittest.TestCase):
	def test_SimpleFileLoading(self):
		dirname = os.path.dirname(__file__)
		filename = os.path.join(dirname, 'TestData\eeg1_1.dat')
		print(filename)
		file=b2k.BCI2kReader(filename)
		self.assertIsNotNone(file)
		file.close()
			
			

if __name__ == "__main__":
	unittest.main()
