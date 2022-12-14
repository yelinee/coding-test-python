# https://www.acmicpc.net/problem/1157
import sys
word = list(sys.stdin.readline().strip().upper())
word_list = list(set(word))
count_list = []
for i in word_list:
  count_list.append(word.count(i))

if count_list.count(max(count_list)) > 1:
  print('?')
else:
  idx = count_list.index(max(count_list))
  print(word_list[idx])

# Mississipi