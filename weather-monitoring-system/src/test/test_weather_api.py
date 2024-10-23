import unittest
from weather_api import fetch_weather_data

class TestWeatherAPI(unittest.TestCase):
    def test_weather_data(self):
        data = fetch_weather_data()
        self.assertTrue(len(data) > 0)

if __name__ == '__main__':
    unittest.main()
