'''
Created on Apr 15, 2014

@author: r24mille
'''

import math
import operator

import Pmf
import chapter_one.first_ans as first
import matplotlib.pyplot as pyplot
import thinkstats

def AllModes(hist, rev=False):
    """
    Returns a list of value-frequency pairs in descending order
    
    Arguments:
    hist -- a Hist object
    """
    getfreq = operator.itemgetter(1)
    return sorted(hist.Items(), key=getfreq, reverse=rev)

def Mode(hist):
    """Returns the mode of a sequence
    
    Arguments:
    t -- a Hist object
    """
    max_freq = hist.MaxLike()
    index_maxfreq = hist.Freqs().index(max_freq)
    return hist.Values()[index_maxfreq]


def PmfMean(pmf):
    """Finds the mean of a sample through the PMF rather than by summing and 
    dividing by the number of elements in the sample.
    
    Arguments:
    pmf -- probability mass function
    """
    mu = 0.0
    d = pmf.GetDict()
    for val, prob in d.iteritems():
        mu += val * prob
    return mu


def PmfVar(pmf):
    """Finds the variance of a sample through the PMF rather than by summing 
    the squared distances from mean.
    
    Arguments:
    pmf -- probability mass function
    """
    var = 0.0
    mu = PmfMean(pmf)
    d = pmf.GetDict()
    for val, prob in d.iteritems():
        var += prob * math.pow((val-mu), 2)
    return var


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
    

def RemainingLifetime(pmf, age):
    """Returns the lifetime distribution function corresponding to function 
    parameters.
    
    Keyword arguments:
    pmf -- probability mass function of deaths
    age -- current age under consideration
    """
    upper_bound = 100
    lifetime_pmf = Pmf.Pmf({})
    for yr in range(age, upper_bound):
        death_dict_gt_yr = {val:prob for val, prob in pmf.Items() if val > yr}
        survival_yr = sum(death_dict_gt_yr.values())
        lifetime_pmf.Set(yr, survival_yr)
    return lifetime_pmf
    
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
    firstsHist = Pmf.MakeHistFromList(firsts.lengths)
    othersHist = Pmf.MakeHistFromList(others.lengths)
    print "Mode of first child gestation is", Mode(firstsHist), "weeks"
    print "Mode of other child gestation is", Mode(othersHist), "weeks"
    print "AllModes function", AllModes(firstsHist, rev=True)
    
    # Exercise 2.4 (worded poorly, lifetime_pmf is not a PMF but I don't know
    # what the quesetion is asking.
    deaths = [85, 72, 80, 95, 86, 87, 86, 82, 81, 74, 86, 65, 78, 77, 77, 56, 
                 80, 75, 74, 72, 73, 88, 84, 81, 92, 68, 71, 77, 75, 81, 86]
    death_pmf = Pmf.MakePmfFromList(deaths)
    age = 29 
    lifetime_pmf = RemainingLifetime(death_pmf, age)
    print "Lifetime PMF", lifetime_pmf.Items()     
    # vals, probs = lifetime_pmf.Render()
    # rectangles = pyplot.bar(vals, probs)
    # pyplot.show()
    
    # Exercise 2.5
    firsts_pmf = Pmf.MakePmfFromList(firsts.lengths)
    print "Mean of first child gestation using conventional method", \
          first.Mean(firsts.lengths), "and PMF method", PmfMean(firsts_pmf)
    print "Variance of first child gestation using conventional method", \
          thinkstats.Var(firsts.lengths), "and PMF method", PmfVar(firsts_pmf)
          
    # Exercise 2.8
    # The mean gestation of first child births is 38.6 weeks while the mean 
    # gestation of other child births is 38.5 weeks, a difference of 0.5 days. 
    # Because the standard deviation of first child gestation and other child 
    # gestation is 2.8 weeks and 2.6 weeks respectively, the difference in 
    # mean gestations is not necessarily statistically significant.
    #
    # Looking at the probability distribution of both gestations, the mode 
    # (ie. "on time") for both is 39 but the kurtosis (ie. "peakedness") of the
    # probability mass function (PMF) gives some indication of a significant 
    # result. The first child gestation PMF is less peaky than subsequent 
    # children, meaning that although both have the same mode and similar 
    # variance, the PMF of other child gestation is peaked more sharply at 
    # week 39. First babies are  8.4% more likely to be born early than others,
    # 10.3% less likely to be born on time, and 65.8% more likely to be born 
    # late. Subsequent children gestations more predictably deliver "on time."
    
if __name__ == "__main__":
    main()
