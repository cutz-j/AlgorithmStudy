from sys import stdin
from collections import deque

N = 8
DICT = {}

## i inclusive, j exclusive
def flip_part( string, i, j):
	# new_string = "{}{}{}".format( string[ :i], ''.join( reversed( string[i:j])), string[j:] )
	new_string = "{}{}{}".format( string[ :i], string[ j-1: (i-1 if i != 0 else None):-1], string[j:] )
	return new_string

def cache_up():
	global N, DICT
	q = deque()
	root = "01234567"
	q.append( root)
	DICT[ root] = 0
	while len( q) != 0:
		s = q.popleft()
		prev_len = DICT[ s] 
		## do for eahch near node of s
		for i in range( 8):
			for j in range( i+2, 8+1):
				# new_s = "{}{}{}".format( s[ :i], s[ j-1: (i-1 if i != 0 else None):-1], s[j:] )
				new_s = s[ :i] + s[ j-1: (i-1 if i != 0 else None):-1] + s[j:]
				if new_s not in DICT:
					DICT[ new_s] = prev_len+1
					q.append( new_s)


def convert( ls):
	output_ls = [-1 for x in range( 8)]
	for i in range( len( ls)):
		item = ls[ i]
		cnt = 0
		for other in ls:
			if other < item:
				cnt += 1
		output_ls[ i] = cnt
	for i in range( len( ls), 8):
		output_ls[ i] = i
	return "".join( map( str, output_ls) )



def parse():
	global N, DICT, SAMPLE
	cache_up()
	TC = int( stdin.readline().strip())
	for x in range( TC):
		N =  int( stdin.readline().strip())
		input_ls = [-1 for x in range( N)]	
		ls = stdin.readline().split()
		ls.reverse()
		for i in range( N):
			input_ls[ i] = int( ls.pop())
		output_string = convert( input_ls)
		print( DICT[ output_string])

parse()
