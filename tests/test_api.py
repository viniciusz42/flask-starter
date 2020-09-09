import unittest
from app import start_server

class Test(unittest.TestCase):

    def setUp(self):
        self.server = start_server().test_client()
