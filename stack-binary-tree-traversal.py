from  __future__ import print_function
import sys
import heapq
lines = []
while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    else:
        lines.append(line)
n,m,k = map(int, lines[0].split(','))

matrix = [[i*j for j in range(1, m+1)]  for i in range(1, n + 1)]
return heapq.merge(*matrix)[k-1]