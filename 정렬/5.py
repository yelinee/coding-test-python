# https://www.acmicpc.net/problem/5988

import sys
n = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(n)]
for i in nums:
  if (i % 2 == 0):
    print('even')
  else:
    print('odd')
