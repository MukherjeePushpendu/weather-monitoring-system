ALERT_THRESHOLD = 35

def check_alerts(processed_data):
    for data in processed_data:
        if data['temp'] > ALERT_THRESHOLD:
            print(f"Alert! High temperature detected in {data['city']}: {data['temp']}°C")
