import requests
from datetime import datetime
from statistics import mean

class Weather:
    base_url = 'https://api.openweathermap.org/data/2.5/'
    defualt_params = {
        'lang': 'ru',
        'units': 'metric',
        'appid': '4268c90514f862fd3dd658ada482282f'
    }

    def request(self, weather_type, city):
        url = self.base_url + weather_type + city
        params = self.defualt_params
        response = requests.get(url, params=params)
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json; charset=utf-8"
        data = response.json()
        return response

    def current_weather(self, city):
        with self.request('weather?q=', city) as response:
            data = response.json()
            assert data['name'] == city
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            temp_max = data['main']['temp_max']
            temp_min = data['main']['temp_min']
            description = data['weather'][0]['description']
            current_date = datetime.now().date()
            print(f'\n В городе {city} {current_date} {description}, температура воздуха: {temp}°С. \n',
                  f'Ощущается как {feels_like}°С. \n',
                  f'Максимальная темперутура {temp_max}°С. \n',
                  f'Минимальная температура {temp_min}°С. \n')

    def get_weather_for_5day(self, city):
        with self.request('forecast?q=', city) as response:
            assert response.status_code == 200
            assert response.headers['Content-Type'] == "application/json; charset=utf-8"
            data = response.json()
            assert len(data['list']) == 40
            temp1 = data['list'][1]['main']['temp']
            dt_txt1 = data['list'][1]['dt_txt']
            temp2 = data['list'][9]['main']['temp']
            dt_txt2 = data['list'][9]['dt_txt']
            temp3 = data['list'][17]['main']['temp']
            dt_txt3 = data['list'][17]['dt_txt']
            temp4 = data['list'][25]['main']['temp']
            dt_txt4 = data['list'][25]['dt_txt']
            temp5 = data['list'][33]['main']['temp']
            dt_txt5 = data['list'][33]['dt_txt']
            temp_lst = [temp1, temp2, temp3, temp4, temp5]
            awg_temp = mean(temp_lst)
            print(f'\n В городе {city} средняя температура за 5 дней =', '%.2f' % awg_temp, '°С. \n',
                  f'{dt_txt1} температура воздуха: {temp1}°С. \n',
                  f'{dt_txt2} температура воздуха: {temp2}°С. \n',
                  f'{dt_txt3} температура воздуха: {temp3}°С. \n',
                  f'{dt_txt4} температура воздуха: {temp4}°С. \n',
                  f'{dt_txt5} температура воздуха: {temp5}°С.')
