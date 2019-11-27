# 4.1 
def major(matrix):
    N = len(matrix)
    majority =-1
    majority_count =0
    for index in range(N):
        element = matrix[index]
        count =0
        for index1 in range(N):
            if matrix[index1]== element:
                count+=1
        if count > majority_count:
            majority = matrix[index]
            majority_count = count
            
    print(majority)
    print(majority_count)
            
mrx = [1,1,2,3,3,3,3,4,4,4]
major(mrx)

# 4.2
def major1(matrix):
    N = len(matrix)
    count = [0*x for x in range(101)]
    for index in range(N):
        count[matrix[index]]+=1
    majority = 0
    for index1 in range(101):
        if count[index1]> count[majority]:
            majority = index1
    print(majority)
    
    
    
mrx = [1,1,2,3,3,3,3,4,4,4]
major1(mrx)


#4.3 Moving average
def moving_avg(matrix,M):
    ret = []
    N = len(matrix)
    for index in range(M-1,N):
        mov_sum=0
        for mov_index in range(M):
            mov_sum+=matrix[index-mov_index]
        
        ret.append(mov_sum/M)
    print(ret)
    
mrx = [1,1,2,3,3,3,3,4,4,4]
moving_avg(mrx,3)
    

# 4.4 
def moving_avg1(matrix,M):
    ret = []
    N = len(matrix)
    mov_sum=0
    for index in range(0,M-1):
        mov_sum+=matrix[index]
    for index1 in range(M-1,N):
        mov_sum+=matrix[index1]
        ret.append(mov_sum/M)
        mov_sum-=matrix[index1-M+1]
    print(ret)
    
mrx = [1,1,2,3,3,3,3,4,4,4]
moving_avg1(mrx,3)
    

# 4.5
#INF = 987654321
#menu=[]
#out_menu = [False for x in range(len(menu))]
#def menu_finder(menu):
#    if 
    
# 4.6
def factor(N):
    if N==1:
        print("no prime")
    output= []
    for div in range(2,N):
        while(N%div ==0):
            N = N/div
            output.append(div)
    print(output)

N= 15
factor(N)
    
    
# 4.7
def firstindex(matrix,element):
    for index in range(len(matrix)):
        if matrix[index]==element:
            return index
    return -1

mrx = [1,2,3,4,5]
print(firstindex(mrx,7))



# 4.8 s

def selection_srt(matrix):
    for index in range(len(matrix)):
        min_index=index
        for index1 in range(index+1,len(matrix)):
            if matrix[min_index]> matrix[index1]:
                min_index=index1
        matrix[index],matrix[min_index] = matrix[index],matrix[min_index]
        
    return matrix
        
        
def insertion_srt(matrix):
    for index in range(len(matrix)):
        j = index
        while(j>0 and matrix[j-1] > matrix[j]):
            matrix[j],matrix[j-1] = matrix[j-1],matrix[j]
            j-=1
    return matrix
marx =[5,4,3,2,1]

print(insertion_srt(marx))
print(selection_srt(marx))
        

    
# 4.9
def inefficientmaxsum(matrix):
    N = len(matrix)
    ret =matrix[0]
    for i in range(N):
        for j in range(i+1,N):
            part_sum=0
            for k in range(i,j):
                part_sum+=matrix[k]
            ret = max(ret,part_sum)
    print(ret)
    
marx= [-1,-2,-3,-4,-5]

inefficientmaxsum(marx)

# 4.10
def bettermaxsum(matrix):
    N = len(matrix)
    ret=matrix[0]
    for i in range(N):
        part_sum=0
        for j in range(i,N):
            part_sum+=matrix[j]
            ret = max(ret,part_sum)
    print(ret)

bettermaxsum(marx)    

# 4.11
def fastmaxsum(matrix,lo,hi):
    if lo==hi:
        return matrix[lo]
    
    part_sum=0
    mid = int((lo+hi)/2)
    left = matrix[lo]
    right= matrix[hi]
    for i in range(lo,mid,-1):
        part_sum+=matrix[i]
        left = max(left,part_sum)
    part_sum=0
    for j in range(mid+1,hi):
        part_sum+=matrix[j]
        right = max(right,part_sum)
        
    single = max(fastmaxsum(matrix,lo,mid),fastmaxsum(matrix,mid+1,hi))
    return max(left+right,single)

print(fastmaxsum(marx,0,4))


#4.12
def fastestmaxsum(matrix):
    N = len(matrix)
    ret=matrix[0]
    psum=0
    for i in range(N):
        psum=max(psum,0)+matrix[i]
        ret = max(psum,ret)
    print(ret)
    
    
fastestmaxsum(marx)
    
    
    
    
