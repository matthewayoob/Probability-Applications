# Name: Matthew Ayoob
import numpy as np

def gen_ber(p:float = 0.3) -> int:
    """
    :param p: The probability of success on a single trial.
    :return: A success (a 1) with probability p, and a fail (a 0) 
    with probability 1 - p.
    """
    assert 0 <= p <= 1
    if np.random.rand() < p:
        return 1
    return 0

def gen_bin(n:int = 5, p:float = 0.4) -> int:
    """
    :param n: The number of (independent) trials.
    :param p: The probability of success on a single trial.
    :return: The number of successes in n independent trials,
    where P(success) = p.
    Hint(s):
    1. Use gen_ber(...).
    """
    assert 0 <= p <= 1
    assert n >= 0
    sum = 0
    for trial in range(n):
        sum += gen_ber(p)
    return sum

def gen_geo(p:float = 0.25) -> int:
    """
    :param p: The probability of success on a single trial.
    :return: The number of trials UP TO AND INCLUDING the 
    first success, when P(success) = p.
    Hint(s):
    1. Use gen_ber(...).
    """
    assert 0 <= p <= 1
    trials = 0
    while gen_ber(p) == 0:
        trials += 1
    return trials + 1
            
   
def gen_negbin(r:int = 6, p:float = 0.75) -> int:
    """
    :param r: The number of successes to wait for.
    :param p: The probability of success on a single trial.
    :return: The number of independent trials UP TO AND INCLUDING
    the rth success, where P(success) = p.
    Hint(s):
    1. Use gen_geo(...).
    """
    assert 0 <= p <= 1
    assert r >= 0
    trials = 0
    for i in range(r):
        trials += gen_geo(p)
    return trials

def gen_hypgeo(N:int = 10, K:int = 4, n:int = 5) -> int:
    """
    :param N: The number of total candies in a bag.
    :param K: The number of candies which are kit kats.
    :param n: The number of candies you are allowed to eat.
    :return: The number of kit kats you get when you eat n
    randomly from a bag of N candies, only K of which are 
    kit kats.
    Hint(s):
    1. For this function ONLY, you may use np.random.choice(...).
    If you want to use it, Google the documentation! And note that
    it returns FLOATs even if the array sampled from has INTs. 
    2. Make sure your return value is an integer, not a float like 3.0.
    """
    assert N >= 1 and K >= 1 and n >= 1
    assert N >= K and n <= N
    kitkats = K
    total = N
    res = 0
    for i in range(n):
        if gen_ber(kitkats/N): 
            res += 1 
            kitkats -= 1
        total -= 1
    return res

def gen_poi(lambduh:float = 3.2) -> int:
    """
    :param lambduh: The historical average of events occurring in
    a unit of time.
    :return: The number of events that happened in a Poisson process
    with parameter lambduh in one unit of time.
    Hint(s):
    1. Like in lecture, remember how a Poisson rv was created out
    of a binomial RV. Let n = 2000 for your approximation!
    2. Use gen_bin(...).
    """
    assert lambduh >= 0
    return gen_bin(2000, lambduh/2000)

def gen_arb(ps=np.array([0.1, 0.3, 0.4, 0.2])):
    """
    :param ps: A (finite) single dimensional np array of 
    probabilities that sum to 1.
    :return: A random index with the appropriate probabilities.
    For example, return 0 with probability 0.1, 1 with probability 0.3,
    2 with probability 0.4, and 3 with probability 0.2.
    Again, you can only use np.random.rand() which generates a random
    float from [0, 1) (basically the same as [0, 1]).
    Hint(s):
    1. Try creating an array of the cumulative distribution function,
    e.g., [0.1, 0.4, 0.8, 1.0] which gives the probability of being
    less than or equal to the index.
    2. Look into np.cumsum(...)
    """
    assert np.all(ps >= 0)
    assert np.sum(ps) == 1
    sum_arr = np.cumsum(ps)
    num = np.random.rand()
    for i in range(len(ps)):
        if num <= sum_arr[i]:
            return i

if __name__ == '__main__':
    # You can test out things here. Feel free to write anything below.
    def print_some_samples(gen_fn, text, n_samples=10):
        print("{} samples from the {} distribution".format(n_samples, text))
        print([gen_fn() for _ in range(n_samples)])

    print_some_samples(gen_ber, "Ber(p=0.3)")
    print_some_samples(gen_bin, "Bin(n=5,p=0.4)")
    print_some_samples(gen_geo, "Geo(p=0.25)")
    print_some_samples(gen_negbin, "NegBin(r=6, p=0.75)")
    print_some_samples(gen_hypgeo, "HypGeo(N=10, K=4, n=5)")
    print_some_samples(gen_poi, "Poi(lambduh=3.2)")
    print_some_samples(gen_arb, "Arb(ps=[0.1, 0.3, 0.4, 0.2]")
