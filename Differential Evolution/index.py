from pip import main
import my_utility as ut
import constants as cons

def main(cost_func,bounds, popsize, mutate, recombination, maxiter):
    population = ut.init_popula(popsize,bounds)
    ut.solve(cost_func,bounds, popsize, mutate, recombination, maxiter,population)
    return 0



main(cons.cost_func,cons.bounds, cons.popsize, cons.mutate, cons.recombination, cons.maxiter)