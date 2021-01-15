# 보석도둑
import sys
import heapq
sys.stdin = open("week04/jewelrykim/test/3.txt",'r')
jewels, bags = map(int, sys.stdin.readline().split())
jewel_list = [list(map(int, sys.stdin.readline().split())) for _ in range(jewels)]
bag_list = [int(sys.stdin.readline()) for _ in range(bags)]
visited = [True for _ in range(len(jewel_list))]
jewel_list.sort(key= lambda x:(x[0],x[1]))
bag_list.sort()

max_mass = 0
for bag_mass in bag_list:
    count_mass = 0
    index = 0
    for i in range(len(jewel_list)):
        if jewel_list[i][0] < bag_mass and visited[i]:
            count_mass = max(count_mass, jewel_list[i][1])
            index = i
        elif jewel_list[i][0] == bag_mass and visited[i]:
            count_mass = max(count_mass, jewel_list[i][1])
            index = i
            break
        elif jewel_list[i][0] > bag_mass:
            break
    visited[index] = False

    max_mass += count_mass
print(max_mass)


# 힙큐로 구현 // 최대힙에는 무게 꺼낼 가방/ 최소힙에는 전체 가방 