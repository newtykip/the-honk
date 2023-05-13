import unittest
import sys

from primeList import findPrimes

# My code can not be unit tested much with how I have structured it but here's proof I know how to do it I guess :D

class SieveTest(unittest.TestCase):
	def test_sieve(self):
		"""
		Test that the sieve correctly generates a list of primes up until 100.
		"""
		primes = findPrimes(100)
		self.assertEqual(primes, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

if __name__ == "__main__":
	sys.argv.append('-v')
	unittest.main()
