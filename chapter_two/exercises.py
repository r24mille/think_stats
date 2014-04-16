'''
Created on Apr 15, 2014

@author: r24mille
'''

import math
import operator

import first
import thinkstats
import Pmf

def AllModes(hist):
    """
    Returns a list of value-frequency pairs in descending order
    
    Arguments:
    hist -- a Hist object
    """
    
    getfreq = operator.itemgetter(1)
    return sorted(hist.Items(), key=getfreq, reverse=True)

def Mode(hist):
    """Returns the mode of a sequence
    
    Arguments:
    t -- a Hist object
    """
    
    max_freq = hist.MaxLike()
    index_maxfreq = hist.Freqs().index(max_freq)
    return hist.Values()[index_maxfreq]


def Pumpkin(weights):
    """Returns the  mean, variance, and standard deviation of pumpkin 
    weights.
    
    Keyword arguments:
    weights -- an array of pumpkin weights
    """
    mean = thinkstats.Mean(weights)
    variance = thinkstats.Var(weights, mean)
    sd = math.sqrt(variance)
    return mean, variance, sd
    
    
def main():
    """Prints results of calling functions specified in Chapter two 
    exercises
    """
    # Exercise 2.1
    mean, variance, sd = Pumpkin([1, 1, 1, 3, 3, 591])
    print "Mean pumpkin weight is", mean, "lbs"
    print "Variance of pumpkin weight is", variance, "lbs squared"
    print "Standard deviation of pumpkin weight is", sd, "lbs"
    print ""
    
    # Exercise 2.2
    table, firsts, others = first.MakeTables()
    first.ProcessTables(firsts, others)
    firsts_variance = thinkstats.Var(firsts.lengths, firsts.mu)
    others_variance = thinkstats.Var(others.lengths, others.mu)
    print "Mean of first child gestation is", firsts.mu, "weeks"
    print "Variance of first child gestation is", firsts_variance, \
          "weeks squared"
    print "Standard deviation of first child gestation is", \
          math.sqrt(firsts_variance), "weeks"
    print "Mean of other child gestation is", others.mu, "weeks"
    print "Variance of other child gestation is", others_variance, \
          "weeks squared"
    print "Standard deviation of other child gestation is", \
          math.sqrt(others_variance), "weeks"
    print "Difference of mean first child gestation and other child "\
          "gestation is", (firsts.mu - others.mu), "weeks. It is much less "\
          "than the groups' standard deviations."
    
    # Exercise 2.3
    print "Mode of first child gestation is", Mode(Pmf.MakeHistFromList(firsts.lengths)), "weeks"
    print "Mode of other child gestation is", Mode(Pmf.MakeHistFromList(others.lengths)), "weeks"
    print AllModes(Pmf.MakeHistFromList(firsts.lengths))
    
if __name__ == "__main__":
    main()
