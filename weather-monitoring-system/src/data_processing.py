def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def process_weather_data(weather_data):
    processed_data = []
    for data in weather_data:
        temp_celsius = kelvin_to_celsius(data['main']['temp'])
        feels_like_celsius = kelvin_to_celsius(data['main']['feels_like'])
        weather_condition = data['weather'][0]['main']
        processed_data.append({
            'city': data['name'],
            'temp': temp_celsius,
            'feels_like': feels_like_celsius,
            'condition': weather_condition,
            'timestamp': data['dt']
        })
    return processed_data
