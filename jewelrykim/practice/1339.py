# 단어 수학
# 리스트 두개로 하면 될듯 알파벳을 다 가지고 있는 애 -> 그 숫자의 값을 저장, 0~9까지 숫자를 가진애 -> True or False
# 자리수 별로 문자열들을 다 리스트에 넣는 다면?????
# 단어들의 길이순서대로 정렬
import sys
# sys.stdin = open("week04/jewelrykim/practice/1339.txt",'r')
N = int(sys.stdin.readline())
word = [sys.stdin.readline().rstrip() for _ in range(N)]
alphabet_num = {'A':-1, 'B':-1, 'C':-1, 'D':-1, 'E':-1, 'F':-1, 'G':-1, 'H':-1, 'I':-1, 'J':-1, 'K':-1
, 'L':-1, 'M':-1, 'N':-1, 'O':-1, 'P':-1, 'Q':-1, 'R':-1, 'S':-1, 'T':-1, 'U':-1, 'V':-1, 'W':-1, 'X':-1, 'Y':-1, 'Z':-1}
num_true = [True for _ in range(10)]
word_len = []
for string in word:
    word_len.append([string, len(string)])
digits = [[] for _ in range(9)]
for string, length in word_len:
    for i in range(length):
        digits[length-i].append(string[i])
for i in range(8,0,-1):
    if digits[i]!=[]:
        for j in digits[i]:
            if alphabet_num[j]==-1:
                for k in range(9,-1,-1):
                    if num_true[k]:
                        alphabet_num[j] = str(k)
                        num_true[k] = False
                        break
answer = 0   
for string in word:
    word_tonum = []
    for st in string:
        word_tonum.append(alphabet_num[st])
    answer += int(''.join(word_tonum))
print(answer)