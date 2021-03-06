#Set_discard()_remove()_pop()

n = int(input())
s = set(map(int,input().split()[:n]))

num = int(input())
for _ in range(num):
    ip = input().split()
    if ip[0] == 'remove':
        s.remove(int(ip[1]))
    elif ip[0] == 'discard':
        s.discard(int(ip[1]))
    else :
        s.pop()

print(sum(list(s)))

'''
Input (stdin)
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
Your Output (stdout)
4
Expected Output
4
'''
