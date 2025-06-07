Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def count_currency(amount):
...     denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]  # Common denominations
...     currency_count = {}
... 
...     for denom in denominations:
...         if amount >= denom:
...             currency_count[denom] = amount // denom
...             amount %= denom
... 
...     return currency_count
... 
... # Input amount
... amount = int(input("Enter the amount: "))
... 
... # Get currency count
... currency_notes = count_currency(amount)
... 
... # Display result
... print("\nCurrency Count:")
... for denom, count in currency_notes.items():
