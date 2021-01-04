import sys
sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline().rstrip())

classes=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

classes.sort()                          #이 걸 안넣으면 틀린다 ;; [7,7] 같은 놈들 떄문에
classes.sort(key=lambda x : x[1])       #1번 인덱스 기준으로 정렬을 한다는 뜻


answer=[classes[0]]
# print(classes)

for i in range(1, len(classes)):
    if classes[i][0] >= answer[-1][1] :
        answer.append([classes[i][0], classes[i][1]])

# print(answer)
print(len(answer))