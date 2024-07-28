import requests
import json

# Base URL of the GeckoTerminal API
base_url = "https://api.geckoterminal.com/api/v2/networks/ton/tokens"

# Function to get detailed token information from GeckoTerminal by contract address
def get_detailed_token_info(contract_address):
    url = f"{base_url}/{contract_address}/info"
    headers = {
        'Accept': 'application/json'
    }
    print(f"Fetching data from URL: {url}")
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        token_data = data.get('data', {}).get('attributes', {})
        if token_data:
            print(f"Token Address: {contract_address}")
            print(f"Name: {token_data.get('name', 'No data available')}")
            print(f"Symbol: {token_data.get('symbol', 'No data available')}")
        else:
            print("No token data found for the given contract address.")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

# Function to get token price and liquidity info from GeckoTerminal pools
def get_token_pool_info(contract_address):
    pool_url = f"https://api.geckoterminal.com/api/v2/networks/ton/tokens/{contract_address}/pools"
    headers = {
        'Accept': 'application/json'
    }
    print(f"Fetching pool data from URL: {pool_url}")
    response = requests.get(pool_url, headers=headers)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        pools = data.get('data', [])
        for pool in pools:
            attributes = pool.get('attributes', {})
            print(f"\nPool ID: {pool.get('id')}")
            print(f"Token 0: {attributes.get('token_0_name')} ({attributes.get('token_0_symbol')})")
            print(f"Token 1: {attributes.get('token_1_name')} ({attributes.get('token_1_symbol')})")
            print(f"Price (USD): {attributes.get('base_token_price_usd', 'No data available')}")
            print(f"Liquidity (USD): {attributes.get('reserve_in_usd', 'No data available')}")
            print(f"Volume 24h (USD): {attributes.get('volume_usd', {}).get('h24', 'No data available')}")
            print(f"Market Cap: {attributes.get('market_cap_usd', 'No data available')}")
            print(f"Total Supply: {attributes.get('total_supply', 'No data available')}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

# Example usage
print("Information for Lady Pink:")
get_detailed_token_info('EQApjmLolkKzsporbp-Xtdur_lgxin-0A3GwSMcQ91LBe7rs')

print("\nFetching pool information for Lady Pink:")
get_token_pool_info('EQApjmLolkKzsporbp-Xtdur_lgxin-0A3GwSMcQ91LBe7rs')
