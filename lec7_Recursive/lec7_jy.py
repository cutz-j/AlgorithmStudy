TEST = int(input())

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x*y

    str_x = str(x)
    str_y = str(y)

    n = max(len(str(x)), len(str(y)))
    n_2 = int(n / 2)

    #higher bits of each number
    x_h = int(str_x[:-n_2])
    y_h = int(str_y[:-n_2])
    
    #lower bits for each number here
    x_l = int(str_x[-n_2:])
    y_l = int(str_y[-n_2:])


    a = karatsuba(x_h, y_h)
    d = karatsuba(x_l, y_l)
    e = karatsuba(x_h + x_l, y_h + y_l) - a - d

    return a*10**len(str_x) + e*10**(len(str_x) // 2) + d


result = karatsuba(1234, 8765)
print(result)


def hug(members,fans):
    N =[]
    M = []
    for elem in members:
        if elem =="M":
            N.append(1)
        else:
            N.append(0)

    for elem in fans:
        if elem =="M":
            M.append(1)
        else:
            M.append(0)

    return hugs


for _ in range(TEST):
    member = list(input())
    fan = list(input())
    out = hug(member,fan)
    print(out)



    ------


    
TEST = int(input())
# index [ x,y]
def finder(location, char):
    # 3 5 8 situation 
    global board
    three = [[0,0],[0,4],[4,0],[4,4]]
    five = [[0,1],[0,2],[0,3],[1,0],[2,0],[3,0],[4,1],[4,2],[4,3],[1,4],[2,4],[3,4]]
    lr = []
    if location in three:
        if location ==[0,0]:
            # compare three time
            if char == board[0][1]:
                lr.append([0,1])
            if char == board[1][0]:
                lr.append([1,0]) 
            if char ==board[1][1]:
                lr.append([1,1])
            
        elif location == [0,4]: 
           # compare three times 
            if char == board[0][3]:
                lr.append([0,3])
            if char == board[1][3]:
                lr.append([1,3])
            if char ==board[1][4]:
                lr.append([1,4])

        elif location == [4,0]:
           # compare three times 
            if char == board[3][0]:
                lr.append([3,0])
            if char == board[4][1]:
                lr.append([4,1])
            if char ==board[3][1]:
                lr.append([3,1])

        elif location == [4,4]:
            if char == board[4][3]:
                lr.append([4,3])
            if char == board[3][3]:
                lr.append([3,3])
            if char ==board[3][4]:
                lr.append([3,4])
        else:
            return False
    elif location in five:
        if location == [0,1]:
            if char == board[0][0]:
                lr.append([0,0])
            if char == board[0][2]:
                lr.append([0,2])
            if char ==board[1][0]:
                lr.append([1,0])
            if char ==board[1][1]:
                lr.append([1,1])
            if char ==board[1][2]:
                lr.append([1,2])
        elif location == [0,2]:
            if char == board[0][1]:
                lr.append([0,1])
            if char == board[0][3]:
                lr.append([0,3])
            if char ==board[1][1]:
                lr.append([1,1])
            if char ==board[1][2]:
                lr.append([1,2])
            if char ==board[1][3]:
                lr.append([1,3])

        elif location == [0,3]:
            if char == board[0][2]:
                lr.append ([0,2])
            if char == board[0][4]:
                lr.append ([0,4])
            if char ==board[1][2]:
                lr.append ([1,2])
            if char ==board[1][3]:
                lr.append ([1,3])
            if char ==board[1][4]:
                lr.append ([1,4])
        elif location == [1,0]:
            if char == board[0][0]:
                lr.append([0,0])
            if char == board[0][1]:
                lr.append([0,1])
            if char ==board[1][1]:
                lr.append([1,1])
            if char ==board[2][0]:
                lr.append([2,0])
            if char ==board[2][1]:
                lr.append([2,1])
        elif location == [2,0]:
            if char == board[1][0]:
                lr.append([1,0])
            if char == board[1][1]:
                lr.append([1,1])
            if char ==board[2][1]:
                lr.append([2,1])
            if char ==board[3][0]:
                lr.append([3,0])
            if char ==board[3][1]:
                lr.append([3,1])
        elif location == [3,0]:
            if char == board[2][0]:
                lr.append([2,0])
            if char == board[2][1]:
                lr.append([2,1])
            if char ==board[3][1]:
                lr.append([3,1])
            if char ==board[4][0]:
                lr.append([4,0])
            if char ==board[4][1]:
                lr.append([4,1])
            else:
                return False
        elif location == [4,1]:
            if char == board[4][0]:
                lr.append([4,0])
            if char == board[4][2]:
                lr.append([4,2])
            if char ==board[3][0]:
                lr.append([3,0])
            if char ==board[3][1]:
                lr.append([3,1])
            if char ==board[3][2]:
                lr.append([3,2])
        elif location == [4,2]:
            if char == board[4][1]:
                lr.append([4,1])
            if char == board[4][3]:
                lr.append([4,3])
            if char ==board[3][1]:
                lr.append([3,1])
            if char ==board[3][2]:
                lr.append([3,2])
            if char ==board[3][3]:
                lr.append([3,3])
        elif location == [4,3]:
            if char == board[4][2]:
                lr.append([4,2])
            if char == board[4][4]:
                lr.append([4,4])
            if char ==board[3][2]:
                lr.append([3,2])
            if char ==board[3][3]:
                lr.append([3,3])
            if char ==board[3][4]:
                lr.append([3,4])
        elif location == [1,4]:
            if char == board[0][4]:
                lr.append([0,4])
            if char == board[0][3]:
                lr.append([0,3])
            if char ==board[1][3]:
                lr.append([1,3])
            if char ==board[2][3]:
                lr.append([2,3])
            if char ==board[2][4]:
                lr.append([2,4])
        elif location == [2,4]:
            if char == board[1][3]:
                lr.append([1,3])
            if char == board[1][4]:
                lr.append([1,4])
            if char ==board[2][3]:
                lr.append([2,3])
            if char ==board[3][3]:
                lr.append([3,3])
            if char ==board[3][4]:
                lr.append([3,4])
        elif location == [3,4]:
            if char == board[2][3]:
                lr.append([2,3])
            if char == board[2][4]:
                lr.append([2,4])
            if char ==board[3][3]:
                lr.append([3,3])
            if char ==board[4][3]:
                lr.append([4,3])
            if char ==board[4][4]:
                lr.append([4,4])
        else:
           return False
    else:
        if char == board[location[0]-1][location[1]-1]:
            lr.append([location[0]-1,location[1]-1])
        if char == board[location[0]-1][location[1]]:
            lr.append([location[0]-1,location[1]])
        if char == board[location[0]-1][location[1]+1]:
            lr.append([location[0]-1,location[1]+1])
        if char == board[location[0]][location[1]-1]:
            lr.append([location[0],location[1]-1])
        if char == board[location[0]][location[1]+1]:
            lr.append([location[0],location[1]+1])
        if char == board[location[0]+1][location[1]-1]:
            lr.append([location[0]+1,location[1]-1])
        if char == board[location[0]+1][location[1]]:
            lr.append([location[0]+1,location[1]])
        if char == board[location[0]+1][location[1]+1]:
            lr.append([location[0]+1,location[1]+1])
        else:
            return False
    return lr
        
    #  8

for _ in range(TEST):
    board = []
    # board maker
    index = []
    for _ in range(5):
        temp = input()
        board.append(list(temp))
        index+=list(temp)
    board_index = set(index)
    word_count = int(input())
    for _ in range(word_count):
        raw = input()
        word = list(raw)
        # quick index
        global_counter =0
        if len(word)==1 and raw in board_index:
            global_counter =1
            print("%s YES" % raw)
        elif len(word)==1 and raw not in board_index:
            global_counter =0
            print("%s NO" % raw)
        else:
            for x in range(5):
                if not global_counter :
                    for y in range(5):
                        if not global_counter:
                            if board[x][y]==word[0]:
                                count=2
                                out1 = finder([x,y],word[1])
                                if len(word)==2:
                                    if out1:
                                        print("%s YES" % raw)
                                        global_counter +=1
                                        break
                                else:
                                    for index in range(2,len(word)-1):
                                        for elem in out1:
                                            test = finder(elem,word[index])
                                            if out:
                                                count+=1
                                            else:
                                                break
                                            if count==len(word):
                                                print("%s YES" % raw)
                                                global_counter +=1
                                                break
        if not global_counter: