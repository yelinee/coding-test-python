# 동빈이의 큰 수 계산
result = 0
count = 0

n, m, k = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
first = lst[n-1]
second = lst[n-2]