import os
import requests
import time
from datetime import datetime
from termcolor import colored

def get_current_bitcoin_price():
  # Use the CoinGecko API to get the current bitcoin price in US dollars
  url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

  response = requests.get(url)
  data = response.json()

  price = data["bitcoin"]["usd"]

  # Convert the price to a string and remove the commas
  price = str(price).replace(",", "")

  return price

def get_current_ethereum_price():
# Use the CoinGecko API to get the current bitcoin price in US dollars
  url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"

  response = requests.get(url)
  data = response.json()

  price = data["ethereum"]["usd"]

  # Convert the price to a string and remove the commas
  price = str(price).replace(",", "")

  return price

def get_current_monero_price():
  # Use the CoinGecko API to get the current Monero price in US dollars
  url = "https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd"

  response = requests.get(url)
  data = response.json()

  price = data["monero"]["usd"]

  # Convert the price to a string and remove the commas
  price = str(price).replace(",", "")

  return price

def log_prices():
  # Get the current prices of bitcoin and Monero
  bitcoin_price = get_current_bitcoin_price()
  ethereum_price = get_current_ethereum_price()
  monero_price = get_current_monero_price()

  # Open the file in append mode
  with open("prices.txt", "a") as file:
    # Write the current timestamp and prices to the file
    file.write(f"{datetime.now()}: Bitcoin - ${bitcoin_price}, Ethereum - ${ethereum_price}, Monero - ${monero_price}\n")

while True:
  # Clear the screen
  os.system("cls")

 # Convert the price to a float and format it to 2 decimal places
  formatted_monero_price = "{:.2f}".format(float(get_current_monero_price()))
  formatted_ethereum_price = "{:.2f}".format(float(get_current_ethereum_price()))
  formatted_bitcoin_price = "{:.2f}".format(float(get_current_bitcoin_price()))

   # Use the termcolor module to add color and formatting to the output
  print(colored(f"Timestamp: {datetime.now()}", "yellow", attrs=["bold"]))
  print()
  print(colored("Current Bitcoin price:", "blue", attrs=["bold"]))
  print(colored(f"${formatted_bitcoin_price}", "green", attrs=["bold"]))
  print()
  print(colored("Current Ethereum price:", "blue", attrs=["bold"]))
  print(colored(f"${formatted_ethereum_price}", "green", attrs=["bold"]))
  print()
  print(colored("Current Monero price:", "blue", attrs=["bold"]))
  print(colored(f"${formatted_monero_price}", "green", attrs=["bold"]))
 
   # Log the prices to a text file
  log_prices()

  # Sleep for one minute
  time.sleep(20)
