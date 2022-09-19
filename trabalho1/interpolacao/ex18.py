from methods import *
import math

def f(x):
	# return math.pow(x,5)-4*pow(x,2)+2*math.sqrt(x+1)+np.cos(x)
  # return math.exp(math.cos(x)**2) + math.exp(-x**2) + math.log(x)
  return 1.0/(1+25*pow(x,2))

if __name__ == '__main__':
	x = [-0.942, -0.694, -0.618, -0.395, -0.308, -0.131, 0.024, 0.296, 0.358, 0.593, 0.716, 0.918]
	y = []

	for i in x:
		y.append(f(i))

	eqs = spline(x, y)

