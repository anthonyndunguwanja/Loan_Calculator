import unittest
from cal_loan import loan_amount

class LoanCalculator(unittest.TestCase):
    def test_it_works(self):
        self.assertEquals(loan_amount(100000,12,12),100000)

if __name__ == "__main__":
    unittest.main()
    

    

