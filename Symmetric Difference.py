#Symmetric Difference

M=int(input())
x=list(map(int,input().split()[:M]))
N=int(input())
y=list(map(int,input().split()[:N]))

x = set(x)
y = set(y)

c = x.difference(y)
d = y.difference(x)

result = list(c.union(d))

for element in sorted(result):
    print(element)
    
'''
Input (stdin)
4
2 4 5 9
4
2 4 11 12
Your Output (stdout)
5
9
11
12
Expected Output
5
9
11
12
'''
