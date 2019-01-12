import unittest
from BCI2kReader import BCI2kReader as b2k

class TestStartup(unittest.TestCase):
	def TestSimpleFileLoading(self):
		with b2k.BCI2kReader('/TestData/eeg1_1.dat') as file:
			self.assertIsNotNone(file)

if __name__ == "__main__":
	unittest.main()