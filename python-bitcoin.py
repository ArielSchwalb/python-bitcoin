"""
    In this project, I'll create a program that that tells
    you when the value of your Bitcoin falls below $30,000.
    We can assume that 1 Bitcoin is worth $40,000

"""

bitcoin_amount = 1.2
bitcoin_value_usd = 40000

# 1) write a function to calculate bitcoin to usd
def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
  usd_value = bitcoin_amount * bitcoin_value_usd
  return usd_value

investment_in_usd = bitcoinToUSD(bitcoin_amount, bitcoin_value_usd)
if investment_in_usd <= 30000:
  print("Investment below $30,000! SELL!")
else:
  print("Investment above $30,000")