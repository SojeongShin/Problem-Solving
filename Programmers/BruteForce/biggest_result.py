from itertools import permutations
import re
import operator

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}

def solution(expression):
    
    tokens = re.findall(r'\d+|[+\-*]', expression)
    biggest = 0
    
    print(tokens)
    
    for operators in permutations(['+','-','*']):
        cur = tokens[:]
        
        for op in operators:
            stack = []
            i = 0
            while i < len(cur):
                if cur[i] == op:
                    left = int(stack.pop())
                    right = int(cur[i+1])
                    val = operations[op] (left, right)
                    stack.append(str(val))
                    i += 2
                else:
                    stack.append(cur[i])
                    i += 1
            cur = stack
        biggest = max(biggest, abs(int(cur[0])))
        
    
    return biggest