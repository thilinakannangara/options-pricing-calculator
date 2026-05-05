# Options Pricing Calculator

A Python command-line tool that calculates the fair price of a European call or put option using the Black-Scholes model.

## What is Black-Scholes?

Black-Scholes is a mathematical formula developed that calculates the fair price of an options contract. It takes into account the current stock price, strike price, time to expiry, interest rates, and volatility to produce a theoretically correct price.

## Installation

Make sure you have Python installed, then install the one dependency:

```bash
pip install scipy
```

## How to Run

```bash
python3 main.py
```

## Inputs

| Input | Description |
|---|---|
| S — Stock Price | Current market price of the stock |
| K — Strike Price | The price you want to lock in |
| T — Time to Expiry | Time until expiry in years (e.g. 0.5 for 6 months) |
| r — Risk Free Rate | Annual interest rate (e.g. 0.05 for 5%) |
| sigma — Volatility | How much the stock moves (e.g. 0.2 for 20%) |
| Option Type | Enter call or put |

## Example Output

Enter the stock price: 150
Enter the strike price: 160
Enter the time to expiry in years: 1
Enter the risk free rate: 0.05
Enter the volatility: 0.2
Enter option type (call or put): call
The option price is: 10.45

## Built With

- Python 3
- scipy
