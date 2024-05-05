import unittest
import requests

class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        self.token ='y0_AgAAAAAOPzDHAAu7kwAAAAED8QglAAAMn-9Ui-lCXqXUHNn2vnmgVXv5GA'
        self.folder_name = "тест33333332"

    def test_create_folder_positive(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            "Authorization": f"OAuth {self.token}",
        }
        params = {
            "path": self.folder_name,
            "overwrite": "false",
        }

        response = requests.put(url, headers=headers, params=params)
        self.assertEqual(response.status_code, 201)


    def test_create_folder_invalid_token(self):
        invalid_token = 'y0_AgAAAAAOPzDHAAu7kwAAAAED8QglAAAMn-9Ui-lCXqXUHNn2vnmgVX'
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            "Authorization": f"OAuth {invalid_token}",
        }
        params = {
            "path": self.folder_name,
            "overwrite": "false",
        }

        response = requests.put(url, headers=headers, params=params)
        self.assertNotEqual(response.status_code, 201)

    def test_create_folder_invalid_name(self):
        invalid_folder_name = "222"
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            "Authorization": f"OAuth {self.token}",
        }
        params = {
            "path": invalid_folder_name,
            "overwrite": "false",
        }

        response = requests.put(url, headers=headers, params=params)
        self.assertNotEqual(response.status_code, 201)

if __name__ == "__main__":
    unittest.main()
