# 외판원 순회
import sys
sys.stdin = open("week04/jewelrykim/6.txt",'r')

city = int(sys.stdin.readline())
graph = []
for _ in range(city):
    graph.append(list(map(int, sys.stdin.readline().split())))
print(graph)