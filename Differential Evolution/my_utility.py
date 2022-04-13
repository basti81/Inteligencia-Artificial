import numpy as np
import random
import math 


def ensure_bounds(v_donor,ub,lb):
  v_new = []
  for i in range(0,len(v_donor)):
    if v_donor[i] < lb[i]:
      v_new.append(lb[i])
    if v_donor[i] > ub[i]:
      v_new.append(ub[i])
    if lb[i] <= v_donor[i] <= ub[i]:
      v_new.append(v_donor[i])
  return v_new
  
#STEP 1: INITIALIZE A POPULATION
def init_population(np,lb,ub):      #Se inicializa la poblacion con valores al a azar
  print("%--------------- Poblacion ------------ %")  
  population = []        
  for i in range(0,np):            #Agrega a la matriz los difrentes valores
    indv = []
    for j in range(0,len(lb)):
      x=lb[1] + random.uniform(0,1)*(ub[1]-lb[1]) 
      indv.append(x)
    population.append(indv)
    print(indv,"\n")
  print("%--------------- Poblacion ------------ %")  
  return population



def solve(population,t,f_mutate,np,p_recom,ub,lb,cost_obj):
  v_candidates = []
  x_diff = []
  v_donor = []
  
  #Step 3.1 = Mutacion
  for i in range(0,t): 
    gen_scores = []    
    print("-- Generacion ",i+1,"--\n")
    for j in range (np):
      #Generate candidate list
      v_candidates = range(0,np)           #Genera un arreglo con diferentes numeros de 0 a np
      ranid=random.sample(v_candidates,4)  #Escoje 3 candidatos al azar

      #-target vectors-
      #print("--Target Vector--")
      x_1=population[ranid[0]] 
      #print("x_1 = ",x_1)
      x_2=population[ranid[1]]
      #print("x_2 = ",x_2)
      x_3=population[ranid[2]]
      #print("x_3 = ",x_3)
      x_t=population[ranid[3]]
      #print("x_t = ",x_t )
            
      #subtract between x_2, x_3
      x_diff = [x_2_i - x_3_i for x_2_i,x_3_i in zip(x_2,x_3)]
      #multiply x_1 with mutate function 
      v_donor = [x_1_i + f_mutate * x_diff_i for x_1_i, x_diff_i in zip(x_1,x_diff)]       #Se crean los vectores de ruido
      v_donor = ensure_bounds(v_donor,ub,lb)    #Vector ruido
      #print("Donor vector = ",v_donor)
      #Step 3.2 = Recombinacion
      v_trial = []
      rdm_recom = random.uniform(0,1)  #Numero random entre 0 y 1
      
      for k in range(0,len(x_t)):
        if (rdm_recom <= p_recom):
          v_trial.append(v_donor[k])     
        else:
          v_trial.append(x_t[k]) 

      #Step 3.3 = Seleccion
      #Recombinacion de los vectores
      score_trial =  cost_obj(v_trial)
      score_target = cost_obj(x_t)
      if score_trial < score_target:
          population[j] =v_trial
          gen_scores.append(score_trial)
      else:
          gen_scores.append(score_target)
      gen_prom = sum(gen_scores)/np
      gen_best = min(gen_scores)
      gen_sol  = population[gen_scores.index(min(gen_scores))]

    print("Current gen. avg.fitness : ",gen_prom)
    print("Best individual fitness :",gen_best)
    print("Best solution individual :",gen_sol,"\n")
    print("-----------------\n")  
  return gen_sol
