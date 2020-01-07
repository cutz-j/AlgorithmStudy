count = int(input())

for _ in range(count):
    length = int(input())
    memory = input().split(" ")
    memory = list(reversed([int(x) for x in memory]))
    number = [x for x in range(1,length+1)]
    fixed =[]
    for element in memory:
        fixed.append(number.pop(len(number)-1-element))
                    

    answer = list(reversed(fixed))
    print(*answer)