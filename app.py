import requests
import json
import config 

from flask import Flask, render_template, request, redirect
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app)

a_weather = api.model('weather', {'location' : fields.String('Weather location you want to see')})
weathers = []

# TODO: POST to a database, display that database in html
# @app.route("/home")
# def index():
#     return render_template('index.html')

# @app.route('/postweathers', methods=["GET", "POST"])
# def weather():
#     location = request.form["location"]

#     payload = {'q': location}

#     response = requests.get(
#         'http://api.weatherapi.com/v1/current.json?key=' + config.API_KEY + '&q=', 
#         params=payload)
#     return render_template('index.html', response=response.json())

# @app.route('/postweathers', methods=["GET", "POST"])
# def weather():
#     a_weather = request.form["location"]
#     weathers.append(a_weather)
#     return render_template('index.html', response=weathers)



@api.route('/weather', methods=["GET", "POST"])
class Weather(Resource):
    def get(self):
        return weathers

    def post(self):
        a_weather = request.form["location"]
        weathers.append(a_weather)
        return render_template('index.html', response=json.dumps(weathers))

    @app.route("/home")
    def index():
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
