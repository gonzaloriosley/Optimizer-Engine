import numpy as np
from pymoo.core.problem import ElementwiseProblem

from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation

from pymoo.factory import get_termination

from pymoo.optimize import minimize

def main():
    #Problem definition
    class MyProblem(ElementwiseProblem):

        def __init__(self):
            super().__init__(n_var=2,
                            n_obj=2,
                            n_constr=2,
                            xl=np.array([-2,-2]),
                            xu=np.array([2,2]))
        
        def _evaluate(self, x,out,*args, **kwargs):
            f1 = 100* (x[0]**2 + x[1]**2)
            f2 = (x[0]-1)**2 +x[1]**2

            g1 = 2*(x[0]-0.1) * (x[0]-0.9) / 0.18
            g2 = - 20*(x[0]-0.4) * (x[0]-0.6) / 4.8

            out["F"] = [f1, f2]
            out["G"] = [g1, g2]

    problem = MyProblem()

    #Algorithm definition

    algorithm = NSGA2(
        pop_size=40,
        n_offsprings=10,
        sampling=get_sampling("real_random"),
        crossover=get_crossover("real_sbx", prob=0.9, eta=15),
        mutation=get_mutation("real_pm", eta=20),
        eliminate_duplicates=True
    )

    #Termination criteria
    termination = get_termination("n_gen", 40)

    #Resolve
    res = minimize(problem,
                algorithm,
                termination,
                seed = 1,
                save_history=True,
                verbose =True
                )

    X = res.X
    F = res.F