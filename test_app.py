import unittest
import requests
from app import app

class MyHTMLPage(unittest.TestCase):
    def setUp(self):
        self.app=app.test_client()
    def test_page(self):
        response=requests.get('http://127.0.0.1:5000')
        self.assertEqual(response.status_code,200)
    def test_calculate(self):
        response=self.app.post('/',data=dict(shape="sphere",radius=2,height=4))
        self.assertTrue(f'Volume Result:The volume is 33.49333333333333.',response.data)
    def test_calculate2(self):
        response=self.app.post('/',data=dict(shape="cone",radius=2,height=4))
        self.assertTrue(f'Volume Result:The volume is 16.746666666666666.',response.data)

if __name__ == '__main__':
    unittest.main()
