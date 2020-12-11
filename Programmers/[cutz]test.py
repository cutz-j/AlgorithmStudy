import sys
sys.stdout = open('output.txt','w')

res = [1 for i in range(100000)]

print(res)