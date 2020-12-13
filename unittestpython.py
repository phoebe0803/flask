import json
import unittest
from hello import app
class LoginTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_empty_username_password(self):
        print("test_empty_username_password")
        """when param loss some value，then return status code=65535 message]"""
        response = app.test_client().post('/addrec', data={})
        print("response",response)
        json_data = response.data
        print(json_data)
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], 65536, 'data erro')

if __name__ == '__main__':
    unittest.main()