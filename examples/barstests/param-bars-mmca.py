import numpy as np
from prosper.utils.barstest import generate_bars_dict

# Number of datapoints to generate
N = 1000

# Each datapoint is of D = size*size
size = 5

# Probability for the generated bars
p_bar = 1. / size

# Dimensionality of the model
H=2*size     # number of latents
D=size**2    # dimensionality of observed data

# Approximation parameters for Expectation Truncation
Hprime = 7
gamma = 5
 
# Import and instantiate a model
from prosper.em.camodels.mmca_et import MMCA_ET
model = MMCA_ET(D, H, Hprime, gamma)


# Ground truth parameters. Only used to generate training data.
params_gt = {
    'W'     :  10*generate_bars_dict(H),
    'pi'    :  1.0 / size,
    'sigma' :  2.0
}

# Choose annealing schedule
from prosper.em.annealing import LinearAnnealing
anneal = LinearAnnealing(300)
anneal['T'] = [(0, 4.), (.8, 1.)]
anneal['Ncut_factor'] = [(0,0.),(2./3,1.)]
anneal['anneal_prior'] = False