import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('COINGECKO_API_KEY')

# URL of the endpoint to get token information
url = "https://api.coingecko.com/api/v3/coins/markets"

# Parameters for the request
params = {
    'vs_currency': 'usd',
    'ids': 'the-open-network'
}

# Headers for the request
headers = {
    'Accept': 'application/json',
    'X-Cg-Pro-Api-Key': api_key
}

# Make the GET request
response = requests.get(url, params=params, headers=headers)

# Check the HTTP status code
if response.status_code == 200:
    # Print the response in JSON format
    data = response.json()
    for token in data:
        print(f"ID: {token['id']}")
        print(f"Symbol: {token['symbol']}")
        print(f"Name: {token['name']}")
        print(f"Current Price: ${token['current_price']}")
        print(f"Market Cap: ${token['market_cap']}")
        print(f"Market Cap Rank: {token['market_cap_rank']}")
        print(f"Total Volume: ${token['total_volume']}")
        print(f"24h High: ${token['high_24h']}")
        print(f"24h Low: ${token['low_24h']}")
        print(f"24h Price Change: {token['price_change_percentage_24h']}%")
        print(f"Last Updated: {token['last_updated']}")
        print(f"Image: {token['image']}")
else:
    print(f"Error: {response.status_code}")
