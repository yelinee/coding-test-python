# https://www.acmicpc.net/problem/2675
n = int(input())
for _ in range(n):
  times, str = (input().split())
  for i in str:
    print(i*int(times), end='')
  print()