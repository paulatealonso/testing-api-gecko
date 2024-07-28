import requests

# Base URL of the GeckoTerminal API
base_url_geckoterminal = "https://api.geckoterminal.com/api/v2/networks/ton/tokens"

# Function to get detailed token information from GeckoTerminal by contract address
def get_detailed_token_info(contract_address):
    url = f"{base_url_geckoterminal}/{contract_address}/info"
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json().get('data', {}).get('attributes', {})
        token_name = data.get('name', 'No data available')
        token_symbol = data.get('symbol', 'No data available')
        websites = data.get('websites', [])
        print(f"Name: {token_name}")
        print(f"Symbol: {token_symbol}")
        if websites:
            print(f"Website: {websites[0]}")
    else:
        print("Error fetching token data")

# Function to get token price, liquidity, FDV, and volume info from GeckoTerminal pools
def get_token_pool_info(contract_address):
    pool_url = f"https://api.geckoterminal.com/api/v2/networks/ton/tokens/{contract_address}/pools"
    headers = {'Accept': 'application/json'}
    response = requests.get(pool_url, headers=headers)
    if response.status_code == 200:
        data = response.json().get('data', [])
        for pool in data:
            attributes = pool.get('attributes', {})
            price_usd = attributes.get('base_token_price_usd', 'No data available')
            if price_usd != 'No data available':
                price_usd = round(float(price_usd), 4)
            print(f"Price (USD): {price_usd}")
            print(f"Liquidity (USD): {attributes.get('reserve_in_usd', 'No data available')}")
            print(f"Volume 24h (USD): {attributes.get('volume_usd', {}).get('h24', 'No data available')}")
            print(f"FDV (Fully Diluted Valuation): {attributes.get('fdv_usd', 'No data available')}")
    else:
        print("Error fetching pool data")

# Main function to execute the script
def main():
    contract_address = input("Please enter the contract address: ")
    print(f"\nInformation for token with contract address {contract_address}:")
    get_detailed_token_info(contract_address)
    print("\nFetching pool information:")
    get_token_pool_info(contract_address)

# Execute the main function
if __name__ == "__main__":
    main()
