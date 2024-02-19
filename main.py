import requests

ETHERSCAN_API_KEY =  ".................................."  # Replace with your actual key

def get_balance(wallet_address, token_address):
    base_url = "https://api.etherscan.io/api"
    endpoint = f"?module=account&action=tokenbalance&contractaddress={token_address}&address={wallet_address}&tag=latest&apikey={ETHERSCAN_API_KEY}"
    url = base_url + endpoint

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['result']
    else:
        return None  # Handle errors gracefully

if __name__ == "__main__":
    wallet_address = input("Enter your wallet address: ")
    token_address = input("Enter the token address: ")

    balance = get_balance(wallet_address, token_address)

    if balance:
        print(f"Your balance is: {balance}")
    else:
        print("Error fetching balance.")
