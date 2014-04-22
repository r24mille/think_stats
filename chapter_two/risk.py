'''
Created on Apr 17, 2014

@author: r24mille
'''
import Pmf

import chapter_one.first_ans as first

def ProbForRange(pmf, start, end):
    """Returns the probability that a baby will be born in a given range of 
    weeks.
    
    Arguments:
    pmf -- The probability mass function of gestations (in weeks)
    start -- Start of delivery week range under consideration (inclusive)
    end -- End of delivery week range under consideration (inclusive)
    """
    dict_in_range = {val:prob for val, prob in pmf.Items() 
                    if val >= start and val <= end}
    return sum(dict_in_range.values())


def ProbEarly(pmf):
    """Returns the probability that a baby will be born during week 37 or 
    earlier
    
    Arguments:
    pmf -- The probability mass function of gestations (in weeks)
    """
    return ProbForRange(pmf, min(pmf.Values()), 37)
    
    
def ProbOnTime(pmf):
    """Returns the probability that a baby will be born during weeks 38, 39, 
    or 40.
    
    Arguments:
    pmf -- The probability mass function of gestations (in weeks)
    """
    return ProbForRange(pmf, 38, 40)
    
    
def ProbLate(pmf):
    """Returns the probability that a baby will be born during week 41 or 
    later
    
    Arguments:
    pmf -- The probability mass function of gestations (in weeks)
    """
    return ProbForRange(pmf, 41, max(pmf.Values()))


def main():
    """Prints the results of exercises in chapter two"""
    # Process data
    table, firsts, others = first.MakeTables()
    first.ProcessTables(firsts, others)
    
    # Generate PMFs
    firsts_pmf = Pmf.MakePmfFromList(firsts.lengths)
    others_pmf = Pmf.MakePmfFromList(others.lengths)
    
    # Probabilities
    firsts_early_prob = ProbEarly(firsts_pmf)
    firsts_on_time_prob = ProbOnTime(firsts_pmf)
    firsts_late_prob = ProbLate(firsts_pmf)
    others_early_prob = ProbEarly(others_pmf)
    others_on_time_prob = ProbOnTime(others_pmf)
    others_late_prob = ProbLate(others_pmf)
    
    # Output
    print "Probability of early first birth", firsts_early_prob * 100, "%"
    print "Probability of on-time first birth", firsts_on_time_prob * 100, "%"
    print "Probability of late first birth", firsts_late_prob * 100, "%"
    print "Probability of early other birth", others_early_prob * 100, "%"
    print "Probability of on-time other birth", others_on_time_prob * 100, "%"
    print "Probability of late other birth", others_late_prob * 100, "%"
    print "First babies are ", \
          ((firsts_early_prob/others_early_prob) - 1) * 100, \
          "% more likely to be born early than others"
    print "First babies are ", \
          ((firsts_on_time_prob/others_on_time_prob) - 1) * 100, \
          "% more likely to be born on-time than others"
    print "First babies are ", \
          ((firsts_late_prob/others_late_prob) - 1) * 100, \
          "% more likely to be born late than others"


if __name__ == "__main__":
    main()
