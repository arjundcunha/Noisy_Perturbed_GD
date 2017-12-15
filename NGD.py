import sys
import subprocess
import numpy as np
from matplotlib import pyplot as plt

eta=0.1
gam=0.55

def func1(x):
	if x < -2:
		return 3*(x + 4)**2 - 20
	else:
		return x**3

def grad1(x):
	if x < -2:
		return 6*(x + 4)
	else:
		return 3*x**2
		
def func2(x):
	if x > -1:
		return x**3
	elif x <= -1 and x > -3:
		return (3*(x + 2)**5 - 8)/5
	elif x <= -3:
		return (15*(x + 4)**2 - 37)/10
		
def grad2(x):
	hope = 0
	if x > -1:
		hope = 3*x**2
	elif x <= -1 and x > -3:
		hope = 3*(x + 2)**4
	elif x <= -3:
		hope = 3*(x + 4)
	return hope

def noisyGrad(x,lr,iters,function):
	sigma=np.sqrt(np.divide(eta,(1+iters)**gam))
	noise = np.random.normal(0,sigma)
	# print (noise)
	x	= x - lr*(function(x))+noise
	return x

		
lr	= 0.01
x	= 0
Xs	= np.arange(-6, x+0.1, 0.05)
old_f	= np.inf

Ys1	= np.array([])
for xs in Xs:
	Ys1	= np.append(Ys1, func1(xs))

plt.subplot(111)
plt.plot(Xs, Ys1, 'b-')	

itr	= 0
while (old_f > func1(x)) or (itr < 1000) :
	
	itr	= itr + 1
	plt.suptitle('Point movement')
	plt.subplot(111)
	old_f	= func1(x)
	plt.plot(x, func1(x), 'k*')
	x = noisyGrad(x,lr,itr,grad1)
	plt.pause(0.001)
	plt.savefig('frame_1_' + str(itr) + '.png', dpi=50)		
plt.plot(x,func1(x),'ro')
plt.show()
print('Single Saddle: %d' % (itr))
print ("Final Single Saddle X : " + str(x))



# Double Saddle
lr=0.1
x	= 2
Xs	= np.arange(-6, x+0.1, 0.05)
# print (Xs)
old_f	= np.inf

Ys2	= np.array([])
for xs in Xs:
	Ys2	= np.append(Ys2, func2(xs))
	
plt.subplot(111)
plt.plot(Xs, Ys2, 'b-')	
# plt.show()

itr	= 0
while (old_f > func2(x)) or (itr < 1000):
	if x<-3.95 and x>-4.05:
 		break
	if itr%10==0:
		print('Iteration : ',itr)
	itr	= itr + 1
	plt.suptitle('Point movement')	
	plt.subplot(111)
	old_f	= func2(x)
	plt.plot(x, func2(x), 'k*')
	x	= noisyGrad(x,lr,itr,grad2)
	plt.pause(0.001)
	plt.savefig('frame_2_' + str(itr) + '.png', dpi=50)
plt.plot(x,func2(x),'ro')
plt.show()
print('Final Double Saddle X : ' + str(x))

# Shift the frames into a folder and then run the command below:
#	For the single saddle graph
#	convert -delay 10 -reverse -loop 0 `ls -t` one_saddle.gif 
#	For the double saddle graph
#	convert -delay 10 -reverse -loop 0 `ls -t` two_saddle.gif
# This uses ImageMagick.
