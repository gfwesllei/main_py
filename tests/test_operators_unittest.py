
import unittest
import services.Widraw as Widraw
class TestWidraw(unittest.TestCase):

    def should_widraw_when_values_Less_then_balance(self):
        self.assertTrue(Widraw.widraw_alled(value=30.0,balance=40.0))

if __name__ == '__main__':
    unittest.main()