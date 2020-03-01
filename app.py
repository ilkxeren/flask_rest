import requests
import json

from flask import Flask, render_template, request, redirect
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app)

a_weather = api.model('weather', {'location' : fields.String('Weather location you want to see')})
weathers = []

# TODO: POST to a database, display that database in html
# @app.route("/home")
# def index():
#     # weather_data = request.form['/weather']
#     return render_template('index.html')

# @app.route('/postweathers', methods=["GET", "POST"])
# def weather():
#     location = request.form["location"]

#     payload = {'q': location}

#     response = requests.get(
#         'http://api.weatherapi.com/v1/current.json?key=' + config.API_KEY + '&q=', 
#         params=payload)
#     return render_template('index.html', response=response.json())

@api.route('/weather')
class Weather(Resource):
    def get(self):
        return weathers

    @api.expect(a_weather)
    def post(self):
        weathers.append(api.payload)
        return {' result' : 'weather added'}, 201


if __name__ == '__main__':
    app.run(debug=True)
