# https://www.acmicpc.net/problem/1781
# 2109번과 동일한 방식으로 풀이
import heapq

n = int(input())
lst = []
for i in range(n):
  lst.append(list(map(int, input().split())))

lst.sort(key=lambda x: x[0])

p_list = []
for i in lst:
  heapq.heappush(p_list, i[1])

  if (len(p_list) > i[0]):
    heapq.heappop(p_list)

print(sum(p_list))