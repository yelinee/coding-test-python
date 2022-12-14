# https://www.acmicpc.net/problem/11720
n = int(input())
lst = input()
sum = 0
#for문 이용
for i in lst:
  sum+=int(i)

print(sum)

"""
# map 및 sum 함수 이용
n = input()
print(sum(map(int,input())))
"""