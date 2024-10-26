import math
def proportion_confidence_interval(n,p,z):
   sqrt = math.sqrt(p * (1 - p) / n)
   interval = z*sqrt
   interval_tuple = (p-interval,p+interval)
   print(f'interval_tuple is {interval_tuple}')
   return interval_tuple

n= 1150
p=0.48
z= 1.645
proportion_confidence_interval(n,p,z)
