import unittest

from common.variables import TIME, USER, ACCOUNT_NAME, ERROR, ACTION
from server import check_message


class TestServer(unittest.TestCase):
    answer_200 = {'response': 200}
    answer_400 = {'response': 400, ERROR: 'Bad Request'}

    def test_200(self):
        self.assertEqual(check_message({ACTION: 'presence', TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.answer_200)

    def user_wrong(self):
        self.assertEqual(check_message({ACTION: 'presence', TIME: 1.1, USER: {ACCOUNT_NAME: 'Wrong'}}), self.answer_400)

    def user_no(self):
        self.assertEqual(check_message({ACTION: 'presence', TIME: 1.1}), self.answer_400)

    def test_action_wrong(self):
        self.assertEqual(check_message({ACTION: 'Wrong', TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.answer_400)

    def test_action_no(self):
        self.assertEqual(check_message({TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.answer_400)


if __name__ == '__main__':
    unittest.main()
