from collections import Counter

inp = "()(((()))(()()()((((()(((())(()(()((((((()(()(((())))((()(((()))((())(()((()()()()(((())(((((((())))()()(()(()(())(((((()()()((())(((((()()))))()(())(((())(())((((((())())))(()())))()))))()())()())((()()((()()()()(()((((((((()()())((()()(((((()(((())((())(()))()((((()((((((((())()((()())(())((()))())((((()())(((((((((((()()(((((()(()))())(((()(()))())((()(()())())())(()(((())(())())()()(()(()((()))((()))))((((()(((()))))((((()(()(()())())()(((()((((())((((()(((()()(())()()()())((()((((((()((()()))()((()))()(()()((())))(((()(((()))((()((()(()))(((()()(()(()()()))))()()(((()(((())())))))((()(((())()(()(())((()())))((((())))(()(()(()())()((()())))(((()((()(())()()((()((())(()()((())(())()))()))((()(())()))())(((((((()(()()(()(())())))))))(()((((((())((((())((())())(()()))))()(())(()())()())((())(()))))(()))(()((()))()(()((((((()()()()((((((((()(()(())((()()(()()))(())()())()((())))()))()())(((()))(())()(())()))()((()((()(()()())(())()()()((())())))((()()(()()((()(())()()())(((()(()()))))(())))(()(()())()))()()))))))()))))((((((())))())))(()(())())(()())))))(()))()))))))()((()))))()))))(()(()((()())())(()()))))(((())()))())())())(((()(()()))(())()(())(())((((((()()))))((()(()))))))(()))())(((()()(()))()())()()()())))))))))))))(())(()))(()))((()(())(()())(())())(()())(())()()(()())))()()()))(())())()))())())(())((())))))))(())))(())))))()))))((())(()(((()))))(()))()((()(())))(()())(((((()))()())()()))))()))))()))())(()(()()()))()))))))((()))))))))))()((()))((()(())((())()()(()()))()(()))))()()(()))()))(((())))(())()((())(())(()())()())())))))))())))()((())))()))(()))()()))(((((((()))())(()()))(()()(()))()(()((()())()))))))(((()()()())))(())()))()())(()()))()()))))))))(())))()))()()))))))()))()())))()(())(())))))()(())()()(()()))))())((()))))()))))(()(((((()))))))))())))())()(())()()))))(())))())()()())()()())()(()))))()))()))))))))())))((()))()))()))())))()())()()())))())))(()((())()((()))())))))())()(())((())))))))))))())()())(())())())(()))(()))()))())(()(())())()())()()(()))))(()(())))))))(())))())(())))))))())()()(())())())))(())))))()))()(()())()(()))())())))))()()(()))()))))())))))))))()))))()))))))())()())()()))))()())))())))))))))))()()))))()()(((()))()()(())()))))((()))))(()))(())())))(())()))))))(()))()))))(())())))))()))(()())))))))))))))())))))))))()((()())(()())))))))((()))))(())(())))()(()())())))())())(()()()())))()))))))())))))())()()())))))))))))()()(()))))()())()))((()())(()))))()(()))))))))))()())())(((())(()))))())()))()))()))))))()))))))(()))))()))))()(())))(())))(()))())()()(()()))()))(()()))))))))()))(()))())(()()(()(()())()()))()))))))))(())))))((()()(()))())())))))()))())(()())()()))())))()(()()()()))((())())))())()(()()))()))))))))(()))(())))()))))(()(()())(()))))()())())()))()()))())))))))))))())()))))))()))))))))())))))()))))())(()())))(())()))())())))))()()(()()())(()())))()()))(((()))(()()()))))()))))()))))((())))()((((((()()))))))())))))))))))(((()))))))))))))(())())))))())(()))))))(()))((()))())))()(()((()))()))()))))))))))())()))()(()()))))())))())(())()(()))()))())(()))()))))(()()))()()(())))))()))(())(()(()()))(()()())))))(((()))))))()))))))))))))(())(()))))()())())()()((()()))())))))(()))))())))))))()()()))))))))())))()(((()()))(())))))(((())())))))((()))()(()))(()))))(()())))(()))())))))()))))(())(())))()((()))(())())))()()))()))))))))()))(()()()(()()()(()))())(())()())(((()))(())))))))))(((()())))()()))))))))()(())(()))()((((())(())(()())))()))(((())()()()))((()))(()))())())))())))(()))())()())())(()(())())()()()(())))())(())))(())))(())()))()))(()((()))))))))())(()))))))())(()()))()()))()(()(()())))()()(()((()((((((()))(())))()()()))())()))((()()(()))())((()(()(()))(()()))))()())))()))()())))))))()()((()())(())))()))(()))(())(()))())(()(())))()()))))))(((()(((()()))()(()(())())((()()))()))()))()))()(()()()(()))((()())()(())))()()))(((())()()())(())()((()()()()(()(())(()()))()(((((()())))((())))))(()()()))))(((()(())))()))((()((()(())()(()((())))((()())()(()))(((()())()()(()))(())(((()((()())()((())()())(((()()))((()((())(()))(()())(()()()))((()))(())(()((()()())((()))(())))(())(())(())))(()())))(((((()(()(((((()())((((()(()())(())(()()(((())((()(((()()(((()()((((((())))())(()((((((()(()))()))()()((()((()))))()(()()(()((()()))))))(((((()(((((())()()()(())())))))))()))((()()(())))(())(()()()())))))(()((((())))))))()()(((()(()(()(()(()())()()()(((((((((()()())()(()))((()()()()()(((((((()())()((())()))((((((()(()(()(()())(((()(((((((()(((())(((((((((())(())())()))((()(()))(((()()())(())(()(()()(((()(())()))())))(())((((((())(()()())()()(((()(((())(()(((())(((((((()(((((((((()))(())(()(()(()))))((()))()(())())())((()(()((()()))((()()((()(())(())(()((())(((())(((()()()((((((()()(())((((())()))))(())((()(()((())))(((((()(()()())())((())())))((())((()((()()((((((())(((()()(()())())(()(()))(()(()))())())()(((((((()(((()(())()()((())((()(()()((()(()()(((((((((((())((())((((((())((()((((()(()((((()(((((((())()((()))))())()((()((((()(()(((()((()())))(())())(((()(((())((((((()(((((((((()()(())))(()(((((()((((()())))((()((()((()(()()(((())((((((((((((()(((())(()(((((()))(()()(()()()()()()((())(((((((())(((((())))))())()(()()(()(()(((()()(((((())(()((()((()(((()()((()((((())()))()((((())(())))()())(((())(())(()()((()(((()()((((((((((()()(()())())(((((((((())((((()))()()((((())(()((((()(((())())(((((((((((()((((())))(())(()(((()(((()((())(((((()((()()(()(()()((((((()((((()((()(()((()(()((((((()))))()()(((((()((()(()(())()))(())(((((((()((((()())(()((()((()(()))())))(())((()))))(((((((()()()())(()))(()()((()())()((()((()()()(()(()()))(()())(())(((((()(((((((((((()((()(((()(((((((()()((((((()(((((()(()((()(((((())((((((()))((((())((()()((())(((())()(((((()()(((((()((()(()(((((((()(((((()((()((()((())(())((())(()))()()))(()()(()(()()(((((((()(((()(((())()(((((()((((((()())((((())()((()((()(()()())(()))((((()()((((((()((()(()(()((((()((()((())((((((()(()(())((((((()((((((((((()((())()))()(()(()(((((()()()))((())))()(()((((((((((((((()(((()((((()((())((()((()(((()()(()(((()((())(()()())))()(()(()(((((()()(()(()((((()(((((())()(()(()))(((((()()(((()()(())((((((((((((((())((())(((((((((((())()()()(())()(()(()(((((((((())(((()))(()()())(()((((()(())(((((()())(())((((((((())()((((()((((((())(()((()(())(((()((((()))(((((((((()()))((((()(())()()()(())(()((())((()()))()(((())(((((())((((((()()))(((((((((()((((((())))(((((((()((()(()(())))())(()(()))()(((((()())(()))()(()(())(((()))))())()())))(((((()))())()((()(()))))((()()()((((((()))()()((((((((())((()(()(((()(()((())((()())(()((((())(()(((()()()(()(()()))())())((((((((((())())((()))()((())(())(())))())()(()()(())))())(()))(((()(()()(((()(((())))()(((()(())()((((((())()))()))()((((((()(()(((((()())))()))))())()()(((()(((((())((()()(()((()((()(()(()(())))(()()()()((()(())(((()((()))((((()))())(())))())(()))()()()())()))(((()()())()((())))(())(()()()()(()())((()(()()((((())))((()((()(())((()(()((())()(()()(((()())()()())((()))((())(((()()(())))()()))(((()((())()(((((()())(())((())()())())((((((()(()(((((()))(()("


c = Counter(inp)

print(c['('] - c[')'])
