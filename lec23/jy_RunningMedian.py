import bisect
count = int(input())
for _ in range(count):
    memory = input().split(" ")
    N = int(memory[0])
    a = int(memory[1])
    b = int(memory[2])
    memory = [1983]
    printer = 1983
    temp =[1983]
    if N!=1:
        for _ in range(1, N):
            val =( (memory[-1]*a)+b)%20090711
            memory.append(val)
            bisect.insort(temp,val)
            if len(temp)%2 ==0:
              printer+=temp[len(temp)//2 -1]
            else:
              printer+=temp[(len(temp)-1)//2]
    else:
        print(printer%20090711)
    print(printer%20090711)

