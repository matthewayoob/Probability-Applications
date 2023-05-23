# Name: Matthew Ayoob

import numpy as np
import matplotlib.pyplot as plt

def part_a(n:int=21, p:float=0.3, ntrials:int=5000):
    """
    Write code to simulate a ping pong game to n points,
    where the probability of you winning a single point is p.
    You must win by 2; for example, if the score is 21 âˆ’ 20, 
    the game isnâ€™t over yet. Simulate ntrials # of games.

    :param n: The number of points to play to.
    :param p: The probability of YOU winning a single point.
    :param ntrials: The number of trials to simulate.
    :return: returns the probability YOU win the overall game.

    You can ONLY use the function np.random.rand() to generate randomness; 
    this function generates a random float from the interval [0, 1).
    """

    def sim_one_game():
        """
        This is a nested function only accessible by parent sim_prob,
        which we're in now. You may want to implement this function!
        """
        my_score = 0
        other_score = 0
        while my_score < n and other_score < n or abs(my_score - other_score) < 2:
            if np.random.rand() < p:
                my_score += 1
                #print(f"myscore: {my_score}")
            else:
                other_score += 1
                #print(f"other_score: {other_score}")
        if my_score > other_score:
            return 1
        else:
            return 0
        
    # Simulate the failure many times
    my_wins = 0
    for i in range(ntrials):
        my_wins += sim_one_game()
    return my_wins / ntrials

def part_b():
    """
    Make a single plot using matplotlib with the x-axis being p
    for different values of p in {0, 0.04, 0.08,...,0.96, 1.0} 
    and the y-axis being the probability of winning the overall game 
    (use your previous function). Plot 3 â€œcurvesâ€ in different colors, 
    one for each n in {3,11,21}.

    You can code up your solution to part (b) here, but this
    will not be autograded. Make sure to label your axes
    and title your plot appropriately, as well as include a 
    legend! Include your resulting plot in the written submission.

    Notes:
    1. You'll call plt.plot(...) 3 times total, one for each
    n. Make sure your calls are of the form:
    'plt.plot(x_vals, y_vals, "-b", label="n=11")' where "-b" indicates
    blue and "n=11" is to say these set of points is for n=11. You may 
    want to use "-r", "-g", and "-b", a different color for each n.
    2. Use plt.legend(loc="upper left").
    3. Use plt.savefig(...).

    :return: Just saved the plot I made
    """
    

if __name__ == '__main__':
    print(part_a())
    part_b()
