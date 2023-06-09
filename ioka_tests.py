import unittest
import ioka
from dotenv import load_dotenv
import os


class IokaTests(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        ioka.api_key = os.getenv("API_KEY")

    def test_create_order(self):
        pass

if __name__ == "__main__":
    unittest.main()
    


