'''
Created on Apr 17, 2014

@author: r24mille
'''
import Pmf
import chapter_one.first_ans as first
import matplotlib.pyplot as pyplot
import myplot


def ConditionalProb(pmf, week):
    """Returns the probability that a baby will be born during a given week, 
    given that it was not born prior to that week.
    
    Arguments:
    pmf -- probability mass function of gestations
    week -- the week under consideration
    """
    cond_pmf = pmf.Copy()
    rems = [val for val in  pmf.Values() 
            if val >= min(pmf.Values()) and val < week]
    for rem in rems:
        cond_pmf.Remove(rem)
    cond_pmf.Normalize()
    return cond_pmf.Prob(week)


def main():
    """Compute the probability that a baby will be born during Week x, given 
    that it was not born prior to Week x, for all x. Plot this value as a 
    function of x for first babies and others.
    """
    # Process data
    table, firsts, others = first.MakeTables()
    first.ProcessTables(firsts, others)
    
    # Generate PMFs
    firsts_pmf = Pmf.MakePmfFromList(firsts.lengths)
    others_pmf = Pmf.MakePmfFromList(others.lengths)
    
    # Conditional probabilities
    firsts_cond_prob = {}
    for week in range(35, 46):
        firsts_cond_prob[week] = ConditionalProb(firsts_pmf, week)
    others_cond_prob = {}
    for week in range(35, 46):
        others_cond_prob[week] = ConditionalProb(others_pmf, week)
        
    # Plot results
    myplot.Plot(firsts_cond_prob.keys(), firsts_cond_prob.values(),
                label="first babies")
    myplot.Plot(others_cond_prob.keys(), others_cond_prob.values(),
                label="others")
    myplot.Show()


if __name__ == "__main__":
    main()
