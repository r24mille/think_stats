'''
Created on Apr 25, 2014

@author: r24mille
'''
import random

from matplotlib import pyplot
import numpy

from chapter_four import brfss
from chapter_four.exercises import Sample
from chapter_one import first_ans as first
from chapter_three import Cdf
from chapter_two import Pmf
from chapter_two import myplot


def IgnorantMonty():
    """ Simulates a round of a modified Monty Hall problem. Monty opens a door 
    at random and if it reveals a car the player looses.
    
    TODO: This function does a lot of list copying needlessly
    """
    # Initial set of doors
    doors = [0, 1, 2] 
    # Mark winning before game
    winning_door = random.sample(doors, 1)[0]
    # Player randomly selects 1 of 3
    player_rnd1 = random.sample(doors, 1)[0]
    # Remove selected door
    doors_remaining_rnd1 = list(doors)
    doors_remaining_rnd1.remove(player_rnd1)
    # Monty selects at random from doors player did not pick
    monty_rnd1 = random.sample(doors_remaining_rnd1, 1)[0]
    if (monty_rnd1 != winning_door):
        doors_start_rnd2 = list(doors)
        doors_start_rnd2.remove(monty_rnd1)
        # Remove player's initial selection, leaving door they must switch to
        player_rnd2 = list(doors_start_rnd2)
        player_rnd2.remove(player_rnd1) 
        return player_rnd2[0] == winning_door
    else:
        # Monty selecte the car and player looses
        return False
    
    
def PartitionBySex(respondents):
    """Partitions respondents from brfss survey into male, female lists of 
    records
    
    Arguments:
    respondents -- brfss.Respondents object
    """
    males = []
    females = []
    for rec in respondents.records:
        if rec.sex == 1:
            males.append(rec)
        elif rec.sex == 2:
            females.append(rec)
    return males, females
    

def Poincare(selected=5, sz=100, mu=950.0, sigma=50.0):
    """Simulates a baker who chooses n loaves from a distribution with mean 
    mu and standard deviation sigma. Returns the heaviest loaf of bread.
    
    Arguments:
    selected -- number of loaves chosen by baker (ie. n from exercise 
                description)
    sz -- loaves baked her day (ie. number of samples)
    mu -- mean
    sigma -- standard deviation
    """
    loaves = Sample(n=sz, mu=mu, sigma=sigma)
    return max(random.sample(loaves, selected))


def MontyHall():
    """ Simulates a round of the Monty Hall problem and returns the event 
    success/failure result.
    
    TODO: This function does a lot of list copying needlessly
    """
    # Initial set of doors
    doors = [0, 1, 2] 
    # Mark winning before game
    winning_door = random.sample(doors, 1)[0]
    # Player randomly selects 1 of 3
    player_rnd1 = random.sample(doors, 1)[0]
    # Remove selected door
    doors_remaining_rnd1 = list(doors)
    doors_remaining_rnd1.remove(player_rnd1)
    # Monty selects at random from doors player did not pick
    monty_rnd1 = random.sample(doors_remaining_rnd1, 1)[0]
    if (monty_rnd1 != winning_door):
        doors_start_rnd2 = list(doors)
        doors_start_rnd2.remove(monty_rnd1)
    else:
        other_door = list(doors_remaining_rnd1)
        other_door.remove(monty_rnd1)
        doors_start_rnd2 = list(doors)
        doors_start_rnd2.remove(other_door[0])
    # Remove player's initial selection, leaving door they must switch to
    player_rnd2 = list(doors_start_rnd2)
    player_rnd2.remove(player_rnd1) 
    return player_rnd2[0] == winning_door
    

def main():
    """Main method which works through exercises from chapter 5 of "Think 
    Stats"
    """
    # Exercise 5.1
    p_six = 2.0/6.0 # 2 or 6
    p_sum_eight = 1.0/6.0 # Only one success event, given p_six
    print "Probability that sum of dice is 8 and one dice is 6", \
          p_six * p_sum_eight
          
    # Exercise 5.2
    prob_six = 1.0/6.0
    prob_not_six = 1.0 - prob_six
    print "Probability that 100 rolls are all 6", prob_six**100
    print "Probability that 100 rolls are not 6", prob_not_six**100
    
    # Exercise 5.3
    prob_girl = 1.0/2.0
    print "Probability that both children are girls", prob_girl**2
    print "Given that the first child is a girl, the probability that the " \
          "2nd child is a girl is", prob_girl
    print "Given that the old child is a girl, the probability that the " \
          "youngest child is a girl is", prob_girl
    print "Given that the child named Florida is a girl, the probability " \
          "the other child is a girl is", prob_girl
          
    # Exercise 5.4
    n = 1000
    wins = 0.0
    for i in range(0, n):
        if MontyHall():
            wins += 1.0
    print "Probability of player winning by always switching", wins/n
    
    # Exercise 5.5
    wins = 0.0
    for i in range(0, n):
        if IgnorantMonty():
            wins += 1.0
    print "Probability of player winning the modified Monty problem", wins/n
    
    # Exercise 5.6
    loaves = []
    for i in range (0, 365):
        loaves.append(Poincare(selected=4, sz=100, mu=950.0, sigma=50.0))
    poin_mu = numpy.mean(loaves)
    poin_sigma = numpy.std(loaves)
    print "Mean of loaves", poin_mu
    print "Standard deviation of loaves", poin_sigma
    model_loaves = Sample(n=365, mu=950.0, sigma=50.0)
    loaves_cdf = Cdf.MakeCdfFromList(loaves, name="Loaves")
    loaves_model_cdf = Cdf.MakeCdfFromList(model_loaves, name="Model Loaves")
    # myplot.Cdf(loaves_cdf)
    # myplot.Cdf(loaves_model_cdf)
    # myplot.Show(title="Poincare vs. Model")
    
    # Exercise 5.7
    respondents = brfss.Respondents()
    respondents.ReadRecords(data_dir="../chapter_four")
    respondents.Recode()
    men, women = PartitionBySex(respondents)
    men_heights = [rec.htm3 for rec in men if rec.htm3 != "NA"]
    women_heights = [rec.htm3 for rec in women if rec.htm3 != "NA"]
    male_height_cdf = Cdf.MakeCdfFromList(men_heights, "Male Heights")
    female_height_cdf = Cdf.MakeCdfFromList(women_heights, "Female Heights")
    dance_couples = 100
    male_dancer_heights = random.sample(men_heights, dance_couples)
    female_dancer_heights = random.sample(women_heights, dance_couples)
    women_taller = 0
    for i in range (0, dance_couples):
        if female_dancer_heights[i] > male_dancer_heights[i]:
            women_taller += 1
    print "Women taller from sampling", women_taller / float(dance_couples)
    
    # Exercise 5.8
    print "Probability of at least one six", \
          prob_six + prob_six - (prob_six**2)
    
    # Exercise 5.9
    # P(A or B) - P(A and B | A or B)
    

if __name__ == '__main__':
    main()