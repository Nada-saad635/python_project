import unittest 
from my_modoule import square, double


class TestSqure(unittest.TestCase):
    def test1(self):
        # Check that calling 'double(2)' returns 4.
        # This tests if the function correctly computes double of 2.
        
        self.assertEqual(square(2) ,4)# test when 2 is given as input the output is 4.
        self.assertEqual(square(3.0 ), 9,0)
class TestDouble(unittest.TestCase):
    def test1(self):
        self.assertEqual(double(2), 4) 
         # Check that calling 'double(0)' returns 0.
        # This tests if the function correctly computes double of 0, verifying that the function works for edge cases.   
        self.assertEqual(double(0), 0)

# Run all the test cases defined in the module when the script is executed.
# This will automatically discover and run all the test cases defined in the module.        
unittest.main()        