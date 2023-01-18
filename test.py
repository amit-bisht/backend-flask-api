from main import app
import unittest
import requests
class FlaskTest(unittest.TestCase):
    URL="http://127.0.0.1:5000/api/user/"
    REPO_URL="http://127.0.0.1:5000/api/repos/"
    def test_userinfo_success(self,name):
        self.URL+=name
        resp=requests.get(self.URL)
        self.assertEqual(resp.status_code,200)
        print("Test completed")
    def test_userinfo_fail(self,name):
        self.URL+=name
        resp=requests.get(self.URL)
        self.assertEqual(resp.status_code,404)
        print("Test completed")
    def test_user_repo_success(self,name):
        self.REPO_URL+=name
        resp=requests.get(self.REPO_URL)
        self.assertEqual(resp.status_code,200)
        print("Test completed")
    def test_user_repo_fail(self,name):
        self.REPO_URL+=name
        resp=requests.get(self.REPO_URL)
        self.assertEqual(resp.status_code,404)
        print("Test completed")
if __name__=="__main__":
    tester=FlaskTest()
    tester.test_userinfo_success('amit-bisht')
    tester.test_userinfo_fail("wrong-name")
    tester.test_user_repo_success("raj")
    tester.test_user_repo_fail("wrong-name")

