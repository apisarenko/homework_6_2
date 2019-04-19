import requests
import unittest


API_KEY = 'trnsl.1.1.20190419T165520Z.3dd1d0030c5732e4.b90aa506b4a7a5441f07e412f8d7e9d89afa3f69'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


class TestApiYandexTranslator(unittest.TestCase):
    def setUp(self):
        params = {
            'key': API_KEY,
            'text': 'programmer',
            'lang': 'en-ru'
        }
        self.response = requests.get(URL, params=params)

    def test_status(self):
        self.assertEqual(self.response.json()['code'], 200)

    def test_translation(self):
        self.assertEqual(self.response.json()['text'][0], 'программист')

    def test_translation_error(self):
        self.assertNotEqual(self.response.json()['text'][0], 'космонавт')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()