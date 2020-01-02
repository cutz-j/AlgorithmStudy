
MEMORY_RIGHT =["]",")","}"]
MEMORY_LEFT = ["[","(","{"]
count = int(input())
for _ in range(count):
    lr = list(input())
    stack =[]
    #종료조건
    # lr이 비었거나.
    # 잘못된 케이스가 나오거나
    case = True
    while case and lr:
        temp =lr.pop(0)
        if temp in MEMORY_RIGHT:
            if stack:      
                if stack[-1] != MEMORY_LEFT[MEMORY_RIGHT.index(temp)]:
                    case= False
                else:
                    stack.pop()
            else:
                case = False
    
        else:
            stack.append(temp)

    if not stack and case:
        print("YES")
    else:
        print("NO")
