from scipy.stats import norm 
import math

def calculate_d1_d2(S, K, T, r, sigma):
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    return d1, d2

def black_scholes_price(S, K, T, r, sigma, option):
    d1, d2 = calculate_d1_d2(S, K, T, r, sigma)
    if option == "call":
        price = S * norm.cdf(d1) - K * math.exp(-r * T ) * norm.cdf(d2)
    else:
      price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return price