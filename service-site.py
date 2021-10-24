import unittest
import requests
SITE = "https://suchonsite-server.herokuapp.com/"
    
class TestServiceSite(unittest.TestCase):

    def test_unexisting_date(self):
        """
        Testing the site should response with 404 error status code
        if an unexisting date is given as url.
        """
        URL = SITE + f"people/by_date/00-00-0000"
        response = requests.get(URL)
        self.assertEqual(response.status_code, 404)

    def test_invalid_url(self):
        """
        Testing the site should response with 404 error status code
        if an invalid date is given as url.
        """
        URL = SITE + f"people/by_date/invalid-destination"
        response = requests.get(URL)
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
