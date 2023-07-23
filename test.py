import unittest
from console import Console

class Test(unittest.TestCase):

    def test_equals_same_type_two_values(self):
        result = Console.equalsSameType([0, input("ingresa el primer numero:"), input("ingresa el segundo numero:")], "string")
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()
