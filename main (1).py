import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def create_table():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS temperature
                 (date TEXT, time TEXT, temperature REAL)''')
    conn.commit()
    conn.close()


def get_and_insert_temperature():
    url = "https://pogoda.unian.ua/85467-ternopil"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        temperature = 7

        
        conn = sqlite3.connect('weather.db')
        c = conn.cursor()
        now = datetime.now()
        date = now.strftime('%Y-%m-%d')
        time = now.strftime('%H:%M:%S')
        c.execute("INSERT INTO temperature (date, time, temperature) VALUES (?, ?, ?)", (date, time, temperature))
        conn.commit()
        conn.close()
    else:
        print("Не вдалося отримати сторінку з погодою.")

if __name__ == "__main__":
    create_table()
    get_and_insert_temperature()
