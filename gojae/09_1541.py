import sys
sys.stdin = open('input.txt', 'r')

strings = sys.stdin.readline().split('-')
num = []
# print(strings)

for string in strings:
    sum = 0
    s = string.split('+')
    for i in s:
        sum += int(i)
    num.append(sum)

# print(num)
n = num[0]
for j in range(1, len(num)):
    n -= num[j]
print(n)
