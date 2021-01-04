# 잃어버린 괄호
import sys
sys.stdin = open("week04/jewelrykim/9.txt", 'r')
expression = list(map(str, sys.stdin.readline().split('-')))
answer = 0
def split_plus(small_expression:str):
    expression_count = 0
    if '+' in small_expression:
        expession_list = small_expression.split('+')
        for i in expession_list:
            expression_count += int(i)
    else:
        expression_count = int(small_expression)
    return expression_count


answer += split_plus(expression[0])

for i in range(1, len(expression)):
    answer -= split_plus(expression[i])

print(answer)