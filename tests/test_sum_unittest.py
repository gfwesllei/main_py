import unittest
from entity.Person import Person

class TestSum(unittest.TestCase):

    def test_sum(self):
        p = Person("Mmn",20)
        print(f'Name of {p.name} age {p.age}')
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 5")

if __name__ == '__main__':
    unittest.main()