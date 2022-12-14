# https://www.acmicpc.net/problem/11399
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
total = 0
sum = 0
for i in lst:
  sum+=i
  total += sum
print(total)