
import unittest
import primeno

class testPrime(unittest.TestCase):
    def testSinglePrime(self):
        a = 3
        result = primeno.is_prime(a)
        self.assertEquals(result, "Prime")
        
    def testingDoublePrime(self):
        b = 11 
        result = primeno.is_prime(b)
        self.assertEquals(result, "Prime")

if __name__ == "__main__":
    unittest.main()
