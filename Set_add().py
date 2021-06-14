#Set .add()
N = int(input())
countries = set()
for i in range(N):
    countries.add(input())
print(len(countries))

'''
Input (stdin)
7
UK
China
USA
France
New Zealand
UK
France
Your Output (stdout)
5
Expected Output
5
'''
