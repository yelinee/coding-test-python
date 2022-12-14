# acmicpc.net/problem/5585
count = 0
wallet = [500, 100, 50, 10, 5, 1]

n = int(input())
n = 1000 - n

for coin in wallet:
  count += n // coin
  n %= coin

print(count)
  