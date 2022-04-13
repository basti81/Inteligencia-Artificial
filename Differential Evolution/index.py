import numpy as np
import random
import math 
import my_utility as mu


#Funcion objetivo (Prueba)
def fun1(x):
    return sum([x[i]**2 for i in range(len(x))])

#Funcion a implementar
def fun2(x):
    return sum([10**(6*(i-1)/(len(x)-1)) * x[i]**2 for i in range(1,len(x))])

# --Constant---
lb=np.array([-5,-5])  # Lowebound
ub=np.array([5,5])    # UpperBound 
t = 10                 # Number of generation
f_mutate = 0.85       # Mutate function
np = 5                # Tamaño de la poblacion
p_recom = 0.5         # probabilidad de mutacion
cost_obj = fun2


# ------------
def main():
  pop = mu.init_population(np,lb,ub)
  mu.solve(pop,t,f_mutate,np,p_recom,ub,lb,cost_obj)      
  return 0

main()