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


lr=0.1
x = 2
Xs	= np.arange(-6, x+0.1, 0.05)
old_f	= np.inf

g_thres=0.05
t_thres=1
t_noise=-1*t_thres-1

Ys2	= np.array([])
for xs in Xs:
	Ys2	= np.append(Ys2, func1(xs))
	
plt.subplot(111)
plt.plot(Xs, Ys2, 'b-')	
plt.show()
array_y = []
array_x = []

t = 0
while (old_f > func1(x)) or (t < 1000):
	array_y.append(t)
	array_x.append(x + 4)
	if x>-4.05 and x<-3.95:
		break
	if t%10==0:
		print('Iteration : ',t)
	t	= t + 1
	plt.suptitle('Point movement')	
	plt.subplot(111)
	old_f	= func1(x)
	plt.plot(x, func1(x), 'k*')

	del_f=grad1(x)
	if (np.linalg.norm(del_f)<= g_thres) and (t-t_noise>t_thres): 
		print ("Gradient value: " +str(del_f))
		x  = x + 2*np.random.random_sample()-1
		t_noise=t
	else:
		x  = x- lr*del_f
	plt.pause(0.001)
	plt.savefig('frame_1_' + str(t) + '.png', dpi=50)
plt.plot(x,func1(x),'ro')		
plt.show()
print (array_y)
print (array_x)
print('Single Saddle: %d' % (t))
print ("Final Single Saddle X : " + str(x))
# plt.clf()


#Double Saddle
# lr=0.05
# x	= 2
# Xs	= np.arange(-6, x+0.1, 0.05)
# old_f	= np.inf

# g_thres=0.15
# t_thres=1
# t_noise=-1*t_thres-1

# Ys2	= np.array([])
# for xs in Xs:
# 	Ys2	= np.append(Ys2, func2(xs))
	
# plt.subplot(111)
# plt.plot(Xs, Ys2, 'b-')	
# plt.show()

# t = 0
# while (old_f > func1(x)) or (t < 1000):
# 	if x>-4.05 and x<-3.95:
# 		break
# 	if t%10==0:
# 		print('Iteration : ',t)
# 	t	= t + 1
# 	plt.suptitle('Point movement')	
# 	plt.subplot(111)
# 	old_f	= func2(x)
# 	plt.plot(x, func2(x), 'k*')

# 	del_f=grad2(x)
# 	if (np.linalg.norm(del_f)<= g_thres) and (t-t_noise>t_thres): 
# 		# For values to lie between -1 to +1
# 		x  = x + 2*np.random.random_sample()-1
# 		t_noise=t
# 	else:
# 		x  = x- lr*del_f
# 	plt.pause(0.001)
# 	plt.savefig('frame_2_' + str(t) + '.png', dpi=50)
# plt.plot(x,func2(x),'ro')
# plt.show()
# print('Final Double Saddle X : ' + str(x))

# # Shift the frames into a folder and then run the command below:
# #	For the single saddle graph
# #	convert -delay 10 -reverse -loop 0 `ls -t` one_saddle.gif 
# #	For the double saddle graph
# #	convert -delay 10 -reverse -loop 0 `ls -t` two_saddle.gif
# # This uses ImageMagick.
