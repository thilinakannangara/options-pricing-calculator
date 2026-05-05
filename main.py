from black_scholes import black_scholes_price

S = float(input("Enter the stock price: "))
K = float(input("Enter the strike price: "))
T = float(input("Enter the time to expiry in years: "))
r = float(input("Enter the risk free rate: "))
sigma = float(input("Enter the volatility: "))
option = input("Enter option type (call or put): ")

result_1 = black_scholes_price(S, K, T, r, sigma, option)

print(result_1)
