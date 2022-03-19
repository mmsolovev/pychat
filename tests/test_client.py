import unittest

from client import presence, check_answer
from common.variables import TIME, ACTION, USER, ACCOUNT_NAME, ERROR


class TestClient(unittest.TestCase):
    def test_answer(self):
        self.assertRaises(ValueError, check_answer, {ERROR: 'Bad Request'})

    def test_answer_200(self):
        self.assertEqual(check_answer({'response': 200}), '200 : OK')

    def test_answer_400(self):
        self.assertEqual(check_answer({'response': 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_presence(self):
        data = presence()
        data[TIME] = 0
        self.assertEqual(data, {ACTION: 'presence', TIME: 0, USER: {ACCOUNT_NAME: 'Guest'}})


if __name__ == '__main__':
    unittest.main()
