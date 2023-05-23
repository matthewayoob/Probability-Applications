# Name: Matthew Louis Ayoob
import numpy as np

"""
The data for this problem is provided in pokemon.txt and follows the
following format.

Col 1: pokemon_id: A unique identifier for the Pokemon.
Col 2: is_legendary: A 1 if the Pokemon is legendary, and 0 otherwise.
Col 3: height: The height of the Pokemon in meters.
Col 4: weight: The weight of the Pokemon in kilograms.
Col 5: encounter_prob: The probability of encountering this Pokemon 
in the wild grass. Note the sum of this entire column is 1, since when
you make an encounter, exactly one of these Pokemon appears.
Col 6: catch_prob: Once you have encountered a Pokemon, the probability 
you catch it. (Ignore any mechanics of the actual game if youâ€™ve played 
a Pokemon game in the past.)
"""

def part_a(filename:str='data/pokemon.txt'):
    """
    Compute the proportion of Pokemon that are legendary, the average
    height, the average weight, the average encounter_prob, and average 
    catch_prob. 

    :param filename: The path to the csv as described in the pset.
    :return: A numpy array of length 5 with these 5 quantities.

    Notes:
    1. Use np.genfromtxt(...) to load the file. Do NOT hardcode 
    'data/pokemon.txt' as the parameter as we may use other hidden
    files to test your function.
    2. Use np.mean(...) with its axis parameter to compute means in one line.
    """
    arr = np.delete(np.genfromtxt(filename), 0, 1)
    return np.mean(arr, axis = 0)

def part_b(filename:str='data/pokemon.txt'):
    """
    Compute the proportion of Pokemon that are legendary, the average
    height, the average weight, the average encounter_prob, and average 
    catch_prob OF ONLY those Pokemon STRICTLY heavier than the median weight. 

    :param filename: The path to the csv as described in the pset.
    :return: A numpy array of length 5 with these 5 quantities.

    Notes:
    1. Use np.median(...) to compute medians along an axis.
    2. Use np.where(...) to select only certain rows.
    """
    arr = np.delete(np.genfromtxt(filename), 0, 1)
    med_weight = np.median(arr, axis = 0)[2]
    to_add = np.where(arr[0:,2] > med_weight) # grabs the rows with valid weight
    return np.mean(arr[to_add], axis = 0) # calculates avg of specified rows


def part_c(filename:str='data/pokemon.txt', ntrials:int=5000):
    """
    Suppose you are walking around the wild grass, and you wonder: how
    many encounters do you expect to make until you ENCOUNTER each Pokemon 
    (at least) once? 

    :param filename: The path to the csv as described in the pset.
    :param ntrials: How many simulations to run.
    :return: The (simulated) average number of ENCOUNTERS you expect to 
    make, until you ENCOUNTER each Pokemon (at least) once.

    Notes:
    1. You only need to use one of the columns for this part! #col 5
    2. You may want to use np.random.choice(...) with the parameter a
    being np.arange(...) and the parameter p being the data column!
    """
    def sim_one():
        """
        This is a nested function only accessible by parent part_c,
        which we're in now. You may want to implement this function!
        """
        encounters = 0;
        bank = np.zeros(row_len)
        while 0 in bank:
            bank[np.random.choice(np.arange(row_len), None, True, enc_coln)] = 1
            encounters += 1
        return encounters

    # Simulate the failure many times
    arr = np.genfromtxt(filename)
    row_len = len(arr) # amount of rows
    enc_coln = arr[:, 4] # the col of encounter probs
    total_encounters = 0
    for i in range(ntrials):
        total_encounters += sim_one()
    return total_encounters/ ntrials


def part_d(filename:str='data/pokemon.txt', ntrials:int=5000):
    """
    Suppose you are walking around the wild grass, and you wonder: how
    many encounters do you expect to make until you CATCH each Pokemon 
    (at least) once? 

    :param filename: The path to the csv as described in the pset.
    :param ntrials: How many simulations to run.
    :return: The (simulated) average number of ENCOUNTERS you expect to 
    make, until you CATCH each Pokemon (at least) once.

    Notes:
    1. You only need to use two of the columns for this part!
    2. You may want to use np.random.choice(...) with the parameter a
    being np.arange(...) and the parameter p being the data column!
    3. You may want to use np.random.rand(...).
    """
    data = np.genfromtxt(filename)[:, -2:]
    n_pokemon = data.shape[0]

    def sim_one():
        """
        This is a nested function only accessible by parent part_d,
        which we're in now. You may want to implement this function!
        """
        encounters = 0;
        bank = np.zeros(row_len)
        while 0 in bank:
            index = np.random.choice(np.arange(row_len), None, True, enc_coln)
            if (bank[index] != 1):
                bank[index] = 1 if np.random.rand() < catch_coln[index] else 0
            encounters += 1
        return encounters

    # Simulate the failure many times
    arr = np.genfromtxt(filename)
    row_len = len(arr) # amount of rows
    enc_coln = arr[:, 4] # the col of encounter probs
    catch_coln = arr[:, 5]
    total_encounters = 0
    for i in range(ntrials):
        total_encounters += sim_one()
    return total_encounters/ ntrials

if __name__ == '__main__':
    # You can test out things here. Feel free to write anything below.
    print(part_a())
    print(part_b())
    print(part_c())
    print(part_d())
