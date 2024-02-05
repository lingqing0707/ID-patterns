import sys
import numpy as np

def generate_two(n,p,q,s,t):
	C,CC = list([]),list([])
	bit_string = '{:0%db}' % n
	a = bit_string.format(0)
	bit_string1 = '{:0%db}' % 4
	p,q,s,t = bit_string1.format(p),bit_string1.format(q),bit_string1.format(s),bit_string1.format(t)
	
	C = C + ['x,y,z,g,h:BITVECTOR('+str(n)+');']
	CC = CC + ['x,y,z,g,h,xx,yy,zz,gg,hh:BITVECTOR('+str(n)+');']
	
	C = C + ['ASSERT((BVXOR(~((x << 1)['+str(n-1)+':0]),(y <<1)['+str(n-1)+':0]) & BVXOR(~((x << 1)['+str(n-1)+':0]), (z <<1)['+str(n-1)+':0]) & BVXOR(x,BVXOR(y,BVXOR(z,(y<<1)['+str(n-1)+':0])))) = 0b'+a+');']
	CC = CC + ['ASSERT(z = BVPLUS('+str(n)+',x,y));']
	CC = CC + ['ASSERT(zz = BVPLUS('+str(n)+',xx,yy));']
	
	C = C + ['ASSERT((BVXOR(~((z << 1)['+str(n-1)+':0]),(g <<1)['+str(n-1)+':0]) & BVXOR(~((z << 1)['+str(n-1)+':0]), (h <<1)['+str(n-1)+':0]) & BVXOR(z,BVXOR(g,BVXOR(h,(g<<1)['+str(n-1)+':0])))) = 0b'+a+');']
	CC = CC + ['ASSERT(h = BVPLUS('+str(n)+',z,g));']
	CC = CC + ['ASSERT(hh = BVPLUS('+str(n)+',zz,gg));']
	
	C = C + ['ASSERT(x['+str(n-1)+':'+str(n-1-3)+']=0b'+p+');']
	CC = CC + ['ASSERT(BVXOR(x,xx)['+str(n-1)+':'+str(n-1-3)+']=0b'+p+');']
	C = C + ['ASSERT(y['+str(n-1)+':'+str(n-1-3)+']=0b'+q+');']
	CC = CC + ['ASSERT(BVXOR(y,yy)['+str(n-1)+':'+str(n-1-3)+']=0b'+q+');']
	C = C + ['ASSERT(g['+str(n-1)+':'+str(n-1-3)+']=0b'+s+');']
	CC = CC + ['ASSERT(BVXOR(g,gg)['+str(n-1)+':'+str(n-1-3)+']=0b'+s+');']
	C = C + ['ASSERT(h['+str(n-1)+':'+str(n-1-3)+']=0b'+t+');']
	CC = CC + ['ASSERT(BVXOR(h,hh)['+str(n-1)+':'+str(n-1-3)+']=0b'+t+');']
	
	#D = CC
	#D = D + ['ASSERT(BVXOR(z,zz)['+str(n-1-2)+':'+str(n-1-3)+']/=0b00);']
	#C = C + ['ASSERT(z['+str(n-1-2)+':'+str(n-1-3)+']/=0b00);']
	C = C + ['QUERY(FALSE);']
	C = C + ['COUNTEREXAMPLE;']
	CC = CC + ['QUERY(FALSE);']
	CC = CC + ['COUNTEREXAMPLE;']
	#D = D + ['QUERY(FALSE);']
	#D = D + ['COUNTEREXAMPLE;']
	
	filename = 'normal_IDC.cvc'
		
	o = open(filename, 'w')
	for c in C:
		o.write(c)
		o.write('\n')
	o.close()
	
	filename1 = 'specific_IDC.cvc'
	
	o = open(filename1, 'w')
	for cc in CC:
		o.write(cc)
		o.write('\n')
	o.close()
	
p = int(sys.argv[1])
q = int(sys.argv[2])
s = int(sys.argv[3])
t = int(sys.argv[4])

generate_two(5,p,q,s,t)
