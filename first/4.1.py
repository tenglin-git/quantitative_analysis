import math
def proportion_confidence_interval(average,s,se,t):
   first = average-80000
   second = first**2
   third = 1+0.1+ second/s
   forth = math.sqrt(third)
   fifth = t * se * forth
   return fifth

n= 10
# 估计标准误差
se=7032.18
t = 1.645
average = 131880.22
s = 12867879399

interval = proportion_confidence_interval(average, s, se, t)
min = 31579.4 - interval
max = 31579.4 + interval
print(f'min = {min},max = {max}')

