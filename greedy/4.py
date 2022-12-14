  # https://www.acmicpc.net/problem/15903

n, m = map(int, input().split())
lst = list(map(int, input().split()))

for i in range(m):
  smallest = min(lst) # 가장 작은 수 찾기
  lst.remove(smallest)
  small = min(lst) # 두 번째로 작은 수 찾기
  lst.remove(small)
  lst.extend([smallest + small, smallest+small]) # 수 대체

print(sum(lst))
"""
# 우선순위 큐 사용
from sys import stdin
import heapq

n, m = map(int, stdin.readline().split())

# heap 생성
cards = []
card_list = [int(x) for x in stdin.readline().split()]

# heapify() 사용하여 변환 가능
for card in card_list:
    heapq.heappush(cards, card)

for _ in range(m):
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)

    heapq.heappush(cards, card1 + card2)
    heapq.heappush(cards, card1 + card2)

print(sum(cards))
"""