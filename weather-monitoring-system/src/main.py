from weather_api import fetch_weather_data
from data_processing import process_weather_data
from alert_system import check_alerts
from database import store_daily_summary

def main():
    # Fetch weather data for specified locations
    weather_data = fetch_weather_data()
    processed_data = process_weather_data(weather_data)
    
    # Check for alerts
    check_alerts(processed_data)
    
    # Store data in the database
    store_daily_summary(processed_data)

if __name__ == "__main__":
    main()
