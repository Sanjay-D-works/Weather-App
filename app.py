import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

db = SQLAlchemy(app)

@app.route('/')
def index():
    url = 'https://pro.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9e479c2c670336896fda8f9cdb407a34'
    city = 'Las Vegas' 


    r = requests.get(url.format(city)).json()
    weather = {
        'city' : city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }
    print(weather)

    return render_template('weather.html', weather=weather)