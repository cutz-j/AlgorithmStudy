
TEST = int(input())
# index [x,y]
def finder(location,counter):  
    global word_length
    global word
    global global_counter
    
    three = [[0,0],[0,4],[4,0],[4,4]]
    five = [[0,1],[0,2],[0,3],[1,0],[2,0],[3,0],[4,1],[4,2],[4,3],[1,4],[2,4],[3,4]]
    if global_counter:
        return True
    if word_length == counter:
        global_counter+=1
        return True
    
    if location:
        if location in three:
            if location ==[0,0]:
                # compare three time
                if word[counter] == board[0][1]:
                    finder([0,1],counter+1)
                if word[counter] == board[1][0]:
                    finder([1,0],counter+1) 
                if word[counter] ==board[1][1]:
                    finder([1,1],counter+1)
                else:
                    return False
                
            elif location == [0,4]: 
               # compare three times 
                if word[counter] == board[0][3]:
                    finder([0,3],counter+1)
                if word[counter] == board[1][3]:
                    finder([1,3],counter+1)
                if word[counter] ==board[1][4]:
                    finder([1,4],counter+1)
                else:
                    return False
    
            elif location == [4,0]:
               # compare three times 
                if word[counter] == board[3][0]:
                    finder([3,0],counter+1)
                if word[counter] == board[4][1]:
                    finder([4,1],counter+1)
                if word[counter] ==board[3][1]:
                    finder([3,1],counter+1)
                else:
                    return False
            elif location == [4,4]:
                if word[counter] == board[4][3]:
                    finder([4,3],counter+1)
                if word[counter] == board[3][3]:
                    finder([3,3],counter+1)
                if word[counter] ==board[3][4]:
                    finder([3,4],counter+1)
                else:
                    return False
        elif location in five:
            if location == [0,1]:
                if word[counter] == board[0][0]:
                    finder([0,0],counter+1)
                if word[counter] == board[0][2]:
                    finder([0,2],counter+1)
                if word[counter] ==board[1][0]:
                    finder([1,0],counter+1)
                if word[counter] ==board[1][1]:
                    finder([1,1],counter+1)
                if word[counter] ==board[1][2]:
                    finder([1,2],counter+1)
                else:
                    return False
            elif location == [0,2]:
                if word[counter] == board[0][1]:
                    finder([0,1],counter+1)
                if word[counter] == board[0][3]:
                    finder([0,3],counter+1)
                if word[counter] ==board[1][1]:
                    finder([1,1],counter+1)
                if word[counter] ==board[1][2]:
                    finder([1,2],counter+1)
                if word[counter] ==board[1][3]:
                    finder([1,3],counter+1)
                else:
                    return False       
            elif location == [0,3]:
                if word[counter] == board[0][2]:
                    finder ([0,2],counter+1)
                if word[counter] == board[0][4]:
                    finder ([0,4],counter+1)
                if word[counter] ==board[1][2]:
                    finder ([1,2],counter+1)
                if word[counter] ==board[1][3]:
                    finder ([1,3],counter+1)
                if word[counter] ==board[1][4]:
                    finder ([1,4],counter+1)
                else:
                    return False
            elif location == [1,0]:
                if word[counter] == board[0][0]:
                    finder([0,0],counter+1)
                if word[counter] == board[0][1]:
                    finder([0,1],counter+1)
                if word[counter] ==board[1][1]:
                    finder([1,1],counter+1)
                if word[counter] ==board[2][0]:
                    finder([2,0],counter+1)
                if word[counter] ==board[2][1]:
                    finder([2,1],counter+1)
                else:
                    return False
            elif location == [2,0]:
                if word[counter] == board[1][0]:
                    finder([1,0],counter+1)
                if word[counter] == board[1][1]:
                    finder([1,1],counter+1)
                if word[counter] ==board[2][1]:
                    finder([2,1],counter+1)
                if word[counter] ==board[3][0]:
                    finder([3,0],counter+1)
                if word[counter] ==board[3][1]:
                    finder([3,1],counter+1)
                else:
                    return False
            elif location == [3,0]:
                if word[counter] == board[2][0]:
                    finder([2,0],counter+1)
                if word[counter] == board[2][1]:
                    finder([2,1],counter+1)
                if word[counter] ==board[3][1]:
                    finder([3,1],counter+1)
                if word[counter] ==board[4][0]:
                    finder([4,0],counter+1)
                if word[counter] ==board[4][1]:
                    finder([4,1],counter+1)
                else:
                    return False
            elif location == [4,1]:
                if word[counter] == board[4][0]:
                    finder([4,0],counter+1)
                if word[counter] == board[4][2]:
                    finder([4,2],counter+1)
                if word[counter] ==board[3][0]:
                    finder([3,0],counter+1)
                if word[counter] ==board[3][1]:
                    finder([3,1],counter+1)
                if word[counter] ==board[3][2]:
                    finder([3,2],counter+1)
                else:
                    return False
            elif location == [4,2]:
                if word[counter] == board[4][1]:
                    finder([4,1],counter+1)
                if word[counter] == board[4][3]:
                    finder([4,3],counter+1)
                if word[counter] ==board[3][1]:
                    finder([3,1],counter+1)
                if word[counter] ==board[3][2]:
                    finder([3,2],counter+1)
                if word[counter] ==board[3][3]:
                    finder([3,3],counter+1)
                else:
                    return False
            elif location == [4,3]:
                if word[counter] == board[4][2]:
                    finder([4,2],counter+1)
                if word[counter] == board[4][4]:
                    finder([4,4],counter+1)
                if word[counter] ==board[3][2]:
                    finder([3,2],counter+1)
                if word[counter] ==board[3][3]:
                    finder([3,3],counter+1)
                if word[counter] ==board[3][4]:
                    finder([3,4],counter+1)
                else:
                    return False
            elif location == [1,4]:
                if word[counter] == board[0][4]:
                    finder([0,4],counter+1)
                if word[counter] == board[0][3]:
                    finder([0,3],counter+1)
                if word[counter] ==board[1][3]:
                    finder([1,3],counter+1)
                if word[counter] ==board[2][3]:
                    finder([2,3],counter+1)
                if word[counter] ==board[2][4]:
                    finder([2,4],counter+1)
                else:
                    return False
            elif location == [2,4]:
                if word[counter] == board[1][3]:
                    finder([1,3],counter+1)
                if word[counter] == board[1][4]:
                    finder([1,4],counter+1)
                if word[counter] ==board[2][3]:
                    finder([2,3],counter+1)
                if word[counter] ==board[3][3]:
                    finder([3,3],counter+1)
                if word[counter] ==board[3][4]:
                    finder([3,4],counter+1)
                else:
                    return False
            elif location == [3,4]:
                if word[counter] == board[2][3]:
                    finder([2,3],counter+1)
                if word[counter] == board[2][4]:
                    finder([2,4],counter+1)
                if word[counter] ==board[3][3]:
                    finder([3,3],counter+1)
                if word[counter] ==board[4][3]:
                    finder([4,3],counter+1)
                if word[counter] ==board[4][4]:
                    finder([4,4],counter+1)
                else:
                    return False

        else:
            if word[counter] == board[location[0]-1][location[1]-1]:
                finder([location[0]-1,location[1]-1],counter+1)
            if word[counter] == board[location[0]-1][location[1]]:
                finder([location[0]-1,location[1]],counter+1)
            if word[counter] == board[location[0]-1][location[1]+1]:
                finder([location[0]-1,location[1]+1],counter+1)
            if word[counter] == board[location[0]][location[1]-1]:
                finder([location[0],location[1]-1],counter+1)
            if word[counter] == board[location[0]][location[1]+1]:
                finder([location[0],location[1]+1],counter+1)
            if word[counter] == board[location[0]+1][location[1]-1]:
                finder([location[0]+1,location[1]-1],counter+1)
            if word[counter] == board[location[0]+1][location[1]]:
                finder([location[0]+1,location[1]],counter+1)
            if word[counter] == board[location[0]+1][location[1]+1]:
                finder([location[0]+1,location[1]+1],counter+1)
            else:
                return False
for _ in range(TEST):
    board = []
    # board maker
    index = []
    # getting board
    for _ in range(5):
        temp = input()
        board.append(list(temp))
        index+=list(temp)
    #setting board_index to minimize check
    board_index = set(index)
    
    word_count = int(input())
    for _ in range(word_count):
        raw = input()
        word = list(raw)
        # quick index
        global_counter =0
        word_length = len(word)
        
        result =  all(elem in board_index  for elem in word)

        if result:
            for x in range(5):
                if not global_counter :
                    for y in range(5):
                        if not global_counter:
                            # first word exists
                            if board[x][y]==word[0]:
                                out1 = finder([x,y],1)
                            if global_counter:
                                print("%s YES" % raw)
                                break
                                                
            if not global_counter:
                print("%s NO" % raw)
        
        else:
            print("%s NO" % raw)

