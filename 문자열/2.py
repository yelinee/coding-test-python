# https://www.acmicpc.net/problem/8958
n = int(input())
for i in range(n):
  score = 0
  total = 0
  ox_list = list(input())
  for ox in ox_list:
    if ox == 'O':
      score += 1
      total += score
    else:
      score = 0
  print(total)