

# EXAMPLE OF FUNCTION (TEST)
def func1(x):
    # Sphere function, use any bounds, f(0,...,0)=0
    return sum([x[i]**2 for i in range(len(x))])

def func2(x):
    # Beale's function, use bounds=[(-4.5, 4.5),(-4.5, 4.5)], f(3,0.5)=0.
    term1 = (1.500 - x[0] + x[0]*x[1])**2
    term2 = (2.250 - x[0] + x[0]*x[1]**2)**2
    term3 = (2.625 - x[0] + x[0]*x[1]**3)**2
    return term1 + term2 + term3
    
#CONSTANTS 
cost_func = func1                   # Cost function
bounds = [(-1,1),(-1,1)]            # Bounds [(x1_min, x1_max), (x2_min, x2_max),...]
popsize = 10                        # Population size, must be >= 4
mutate = 0.5                        # Mutation factor [0,2]
recombination = 0.7                 # Recombination rate [0,1]
maxiter = 20                        # Max number of generations (maxiter)


