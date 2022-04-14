import pytest
import os

from actions.Weather import Weather


class TestWeather(Weather):

    @pytest.mark.parametrize("city", [
        'Москва',
        'Якутск',
        'Джакарта',
    ])
    def test_get_weather(self, city):
        current_weather = self.current_weather(city)
        return current_weather

    def test_weather_for_5day(self):
        with open('/Users/aisafa/weathers/cityes.txt', 'r') as cityes:
            for city in cityes:
                if not city:
                    break
                city = city.replace('\n', '')
                weather_for_5day = self.get_weather_for_5day(city)
        return weather_for_5day
