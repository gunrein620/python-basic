prices = [1500, 2000, 3000, 4000, 4500]

for i in range(len(prices)):
  prices[i] = prices[i] + prices[i]* 0.05
print(prices)

prices.append(5000)
print(prices[1:-2])