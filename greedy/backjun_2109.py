import heapq
# min heap 구조
# 자식 노드가 부모 노드보다 작음

n = int(input())
lst = []

# 반복해서 리스트에 넣는 형태
for i in range(n):
  lst.append(list(map(int, input().split())))  # map(function, iterable)
  # iterable은 반복 가능한 객체
  # map 함수는 결과로 map 객체를 반환하기 때문에 list()로 형변환

lst.sort(key=lambda x: (x[1]))
# d를 기준으로 정렬
# sorted(list, key): 정렬 결과를 출력
p_list = []  # 우선순위 큐
for i in lst:
  heapq.heappush(p_list, i[0])  # 힙 구조를 유지하면서 삽입
  if (len(p_list) > i[1]):
    heapq.heappop(p_list)

print(sum(p_list))
