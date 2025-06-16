from flask import Flask, jsonify, send_from_directory, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

weather_model_map = {
    "Rain": "https://api.echo3d.com/webar?key=holy-butterfly-0215&entry=1239d368-f0ac-4813-b8d1-fdefb32b52c9",
    "Drizzle": "https://api.echo3d.com/webar?key=holy-butterfly-0215&entry=1239d368-f0ac-4813-b8d1-fdefb32b52c9",
    "Mist": "https://api.echo3d.com/webar?key=holy-butterfly-0215&entry=1239d368-f0ac-4813-b8d1-fdefb32b52c9",
    "Clear": "https://api.echo3d.com/webar?key=holy-butterfly-0215&entry=4e21831a-47f7-42a7-9faf-1b0217fabd60",
    "Clouds": "https://api.echo3d.com/webar?key=holy-butterfly-0215&entry=81154b11-5a00-49f0-ad31-286f641a8c1a",
    "Snow": "https://api.echo3d.com/webar?key=holy-butterfly-0215&entry=ab27791b-cf09-456e-b2a2-4c717a59298a"
}

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/model')

def get_model():
    city = request.args.get("city", default="New York")
    
    # "New York" # Default city, can be modified or passed as a parameter
    key = os.getenv('WEATHER_API_KEY')

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather_condition = data['weather'][0]['main']
        print(f"Weather condition in {city}: {weather_condition}")

        model_url = weather_model_map.get(weather_condition, weather_model_map["Clear"])

        return jsonify({
            "condition": weather_condition,
            "model_url": model_url
        })
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True)