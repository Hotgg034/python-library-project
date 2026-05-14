import unittest
from library import borrow_book, return_book

class TestLibrary(unittest.TestCase):
    def test_borrow_book(self):
        self.assertEqual(borrow_book(True, "Harry Potter"), "You borrowed: Harry Potter")
        self.assertEqual(borrow_book(False, "Harry Potter"), "Not available")

    def test_return_book(self):
        self.assertEqual(return_book("Harry Potter"), "Returned: Harry Potter")
        self.assertEqual(return_book(""), "Error: No title provided")

if __name__ == "__main__":
    unittest.main()
