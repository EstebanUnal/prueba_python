import math;
B = 5;
k = math.log(4/5)/2;
t = 0;
func = 1500/(1 + B*math.exp(-k*t));
print(func)
