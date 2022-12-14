# https://www.acmicpc.net/problem/1181
import sys
# 입력 속도 줄이기 위해 sys 모듈 사용
N = int(sys.stdin.readline())
lst = [sys.stdin.readline().strip() for _ in range(N)]
    # strip(): 공백제거(lstrip, rstrip)
lst = list(set(lst))
lst.sort()
lst.sort(key=len) # 글자수로 정렬

for i in lst:
  print(i)

"""
# sys 이용
for line in sys.stdin:
  lst.append(line)
"""
'''
# input() 이용
for i in range(n):
  lst.append(input())
'''