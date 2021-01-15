# 피보나치 수2
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

with PyCallGraph(output=GraphvizOutput()):
    code_to_profile()
    
import sys
def code_to_profile():
    number = int(sys.stdin.readline())

    dp_table = [0 for _ in range(91)]

    dp_table[1] = 1

    for i in range(2, number+1):
        dp_table[i] = dp_table[i-1] + dp_table[i-2]

    print(dp_table[number])

code_to_profile()
