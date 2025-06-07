Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import requests
... 
... def get_exchange_rate(from_currency, to_currency):
...     url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
...     response = requests.get(url)
...     
...     if response.status_code == 200:
...         data = response.json()
...         if to_currency in data["rates"]:
...             return data["rates"][to_currency]
...         else:
...             print("Invalid target currency.")
...             return None
...     else:
...         print("Error fetching exchange rates.")
...         return None
... 
... def convert_currency(amount, from_currency, to_currency):
...     exchange_rate = get_exchange_rate(from_currency, to_currency)
...     
...     if exchange_rate:
...         converted_amount = amount * exchange_rate
...         print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
...     else:
...         print("Conversion failed.")
... 
... # User input
... from_currency = input("Enter base currency (e.g., USD, INR, EUR): ").upper()
... to_currency = input("Enter target currency (e.g., USD, INR, EUR): ").upper()
... amount = float(input("Enter amount to convert: "))
... 
... # Perform conversion
... convert_currency(amount, from_currency, to_currency)
>>> [DEBUG ON]
>>> [DEBUG OFF]
