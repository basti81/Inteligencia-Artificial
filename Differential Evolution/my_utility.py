import numpy as np
import random
import math 


#Verifica los limites del vector donor 
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
  
#PASO 1: INICIALIZAR POBLACIÓN
def init_population(np,lb,ub):      
  print("%--------------- Poblacion ------------ %")  
  population = []                                       #Crea estructura población
  for i in range(0,np):                                       
    indv = []                                           #Crea estructura individuos
    for j in range(0,len(lb)):  
      x=lb[1] + random.uniform(0,1)*(ub[1]-lb[1])       
      indv.append(x)                                    #Inserta valores aletorios al individuo
    population.append(indv)                             #Inserta los individuos a la poblacion
    print(indv,"\n")
  print("%--------------- Poblacion ------------ %\n")  
  return population                                     #Retorna la población ya poblada



def solve(population,t,f_mutate,np,p_recom,ub,lb,cost_obj):
  v_candidates = []
  x_diff = []
  v_donor = []
  
  #PASO 2: MUTACION
  for i in range(0,t): 
    gen_scores = []    
    print("-- Generacion ",i+1,"--\n")
    for j in range (np):
      #Genera lista de candidatos
      v_candidates = range(0,np)               
      ranid=random.sample(v_candidates,4)      

      #-Vectores de prueba-
      x_1=population[ranid[0]] 
      x_2=population[ranid[1]]
      x_3=population[ranid[2]]
      x_t=population[ranid[3]]

      """"
      print("-- Vectores Objetivos --")
      print("x_1 : ",x_1)   
      print("x_2 : ",x_2) 
      print("x_3 : ",x_3)
      print("x_t : ",x_t )
      """

      #Diferencia entre el vector prueba x_2 y x_3
      x_diff = [x_2_i - x_3_i for x_2_i,x_3_i in zip(x_2,x_3)]
      #Multiplicacion de x_diff con el factor de mutacion mas el vector x_1
      v_donor = [x_1_i + f_mutate * x_diff_i for x_1_i, x_diff_i in zip(x_1,x_diff)] 
      #Vector ruido     
      v_donor = ensure_bounds(v_donor,ub,lb)

      """"
      print("-- Donor Vector --)
      print("v_donor : ",v_donor)
      """

      #PASO 3: RECOMBINACIÓN
      v_trial = []
      rdm_recom = random.uniform(0,1)  #Numero random [0,1]
      
      for k in range(0,len(x_t)):
        if (rdm_recom <= p_recom):     #Verifica que sea menor o igual que la probabilidad de mutacion 
          v_trial.append(v_donor[k])     
        else:
          v_trial.append(x_t[k]) 

      """
      print("--Vectores Prueba --")
      print("v_trial : ",v_trial)
      """    

      #PASO 4: SELECCION
      #Recombinacion de los vectores
      score_trial =  cost_obj(v_trial)  # Evalua el vector de prueba en la funcion de costo 
      score_target = cost_obj(x_t)      # Evalua el vector blanco en la funcion de costo 
      if score_trial < score_target:    # El puntaje de prueba debe ser menor al puntaje del blanco  
          population[j] =v_trial         # Se reemplaza el vector de prueba ya validad por el vector actual
          gen_scores.append(score_trial)    
      else:
          gen_scores.append(score_target)

      gen_prom = sum(gen_scores)/np     
      gen_best = min(gen_scores)        # Se obtiene el menor gen encontrado 
      gen_sol  = population[gen_scores.index(min(gen_scores))]  

    print("Promedio fitness generacion actual : ",gen_prom)
    print("Mejor fitness individual :",gen_best)
    print("Mejor solucion individual :",gen_sol,"\n")
    print("-----------------\n")  
  return gen_sol
