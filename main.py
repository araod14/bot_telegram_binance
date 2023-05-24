import telebot
import time
from binance.client import Client


# Set up the bot
bot = telebot.TeleBot(token='YOUR_BOT_TOKEN')

# Set up the Binance client
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
client = Client(api_key, api_secret)

# Define the function to retrieve the wallet balance and cryptocurrency price
def retrieve_balance_and_price():
    # Retrieve the wallet balance
    balance = client.get_asset_balance(asset='USDT')
    balance = float(balance['free'])
    
    # Retrieve the cryptocurrency price
    symbol = 'BTCUSDT'
    price = client.get_avg_price(symbol=symbol)
    price = float(price['price'])

    # Send a message to the user with the wallet balance and cryptocurrency price
    message = f"Your wallet balance is {balance:.2f} USDT\n"
    message += f"The price of {symbol} is {price:.2f} USDT"
    bot.send_message(chat_id='YOUR_CHAT_ID', text=message)

# Set up the timer to run the function every 5 minutes
while True:
    retrieve_balance_and_price()
    time.sleep(300)
