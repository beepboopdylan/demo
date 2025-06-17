# 1. Make sure Python 3.8+ is installed:
#    macOS: python3 --version
#    Windows: py --version

# 2. Clone the repo
git clone https://github.com/your-repo.git
cd your-repo

# 3. Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Add your OpenWeather API key in a .env file
echo "WEATHER_API_KEY=your_api_key" > .env

# 6. Run the app
python app.py
