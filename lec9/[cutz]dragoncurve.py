import sys

p = -1

def curve(seed, gen):
    if gen == 0:
        print(seed)
        return
    
    for i in range(len(seed)):
        if seed[i] == 'X':
            curve("X+YF", gen-1)
        elif seed[i] == 'Y':
            curve("FX-Y", gen-1)
        else:
            print(seed[i])
            
MAX = 1000000000 + 1
length = [i for i in range(51)]
def precalc():
    length[0] = 1
    # 점화식
    for i in range(1, 51):
        length[i] = min(MAX, length[i-1]*2+2)
        
X = 'X+YF'
Y = 'FX-Y'

def expand(dragon_curve, gen, skip):
    if gen == 0:
        assert(skip < len(dragon_curve))
        return dragon_curve[skip]
    
    for i in range(len(dragon_curve)):
        if dragon_curve[i] == 'X' | dragon_curve[i] == 'Y':
            if skip >= length[gen]:
                skip -= length[gen]
            elif dragon_curve[i] == 'X':
                return expand(X, gen-1, skip)
            else:
                return expand(Y, gen-1, skip)
        elif skip > 0:
            skip-=1
        else:
            return dragon_curve[i]
    return '#'
        
    