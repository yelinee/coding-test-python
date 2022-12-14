# https://www.acmicpc.net/problem/1202
import heapq

n, k = map(int, input().split())
jewel = []
bags = []

for i in range(n):
  jewel.append(list(map(int, input().split())))
for i in range(k):
  bags.append(int(input()))

jewel.sort(key=lambda x: x[0])
bags.sort()

result = []
for j in jewel:
  heapq.heappush(result, j[1])

  if (len(jewel)>j[0]):
    heapq.heappop(result)
  
  

print(jewel)
print(bags)