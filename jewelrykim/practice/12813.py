# 이진수 연산 - 비트 마스크
import sys
sys.stdin = open("week04/jewelrykim/practice/12813.txt",'r')
A = int(sys.stdin.readline().strip(),2)
B = int(sys.stdin.readline().strip(),2)

print(bin(A & B).zfill(100000))
print(bin(A | B).zfill(100000))
print(bin(A ^ B).zfill(100000))
