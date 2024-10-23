import sqlite3

def store_daily_summary(processed_data):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS weather
                 (city TEXT, temp REAL, feels_like REAL, condition TEXT, timestamp INTEGER)''')

    for data in processed_data:
        c.execute("INSERT INTO weather (city, temp, feels_like, condition, timestamp) VALUES (?, ?, ?, ?, ?)", 
                  (data['city'], data['temp'], data['feels_like'], data['condition'], data['timestamp']))
    
    conn.commit()
    conn.close()
