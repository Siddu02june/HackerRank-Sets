#Set_intersection()

E = int(input())
English = list(input().split()[:E])
F = int(input())
French = list(input().split()[:F])
print(len(set(English) &s et(French)))

'''
Input (stdin)
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Your Output (stdout)
5
Expected Output
5
'''
