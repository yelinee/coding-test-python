# https://www.acmicpc.net/problem/1461
from sys import stdin
import heapq

n, m = map(int, stdin.readline().split())
locations = [int(x) for x in stdin.readline().split()]

heapq.heapify(locations)

for _ in range(n/m):
  for i in range(m):
    
    total += heapq.heappop(locations)

print(n, m)
print(locations)
