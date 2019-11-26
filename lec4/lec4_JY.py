# 2869
import math

text = input().split(" ")
numbers = [ int(x) for x in text]

print(math.ceil((numbers[2]-numbers[0])/(numbers[0]-numbers[1])) +1)

# 2798
line1 = input().split(" ")
line1 = [int(x) for x in line1]

line2 = input().split(" ")
line2 = [int(x) for x in line2]
sota =0
for i in range(len(line2)):
    for j in range(i+1, len(line2)):
        for k in range(j+1,len(line2)):
            val = line2[i] +line2[j] +line2[k]
            if val <= line1[1] and line1[1] - val < line1[1]-sota:
                sota = val
print(sota)


#10250
count= int(input())
for _ in range(count):
  line = input().split(" ")
  line = [int(x) for x in line]
  # line[0] = floor , line[1] = range, line[2]=number
  room =((line[2]-1)//line[0])+1
  if not (line[2]%line[0]):
      floor =line[0]
  else:
      floor =(line[2]%line[0])   
  if room <10:
      name = str(floor)+str(0)+str(room)
      print(name)
  else:
      name = str(floor)+str(room)
      print(name)


# 2775
count= int(input())
table1 = [x for x in range(1,15)]
table2 = [int(x*(x+1)/2) for x in range(1,15)]
table3 = [int(x*(x+1)/4+(x)*(x+1)*(2*x+1)/12) for x in range(1,15)]

table = [table1,table2,table3]
for _ in range(count):
    K = int(input())
    N = int(input())
    if K <=2:
        print(table[K][N-1])
    else:
        while len(table)-1<K:
            temp=[sum(table[len(table)-1][:x]) for x in range(1,15)]
            table.append(temp)
        print(table[K][N-1])