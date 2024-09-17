from mealpy import FloatVar, SMA
import numpy as np

def objective_function(solution):
    return np.sum(solution**2)

problem = {
    "obj_func": objective_function,
    "bounds": FloatVar(lb=(-100., )*30, ub=(100., )*30),
    "minmax": "min",
    "log_to": None,
}

## Run the algorithm
model = SMA.OriginalSMA(epoch=100, pop_size=50, pr=0.03)
g_best = model.solve(problem)
print(f"Best solution: {g_best.solution}, Best fitness: {g_best.target.fitness}")