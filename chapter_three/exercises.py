'''
Created on Apr 17, 2014

@author: r24mille
'''
import heapq

import Cdf
from chapter_one import first_ans as first
from chapter_two import Pmf
from chapter_two import myplot
import matplotlib.pyplot as pyplot
import relay


def ConvertTimeToSeconds(time):
    """Return the number of seconds (int) in a given clock time.
    
    Arguments:
    time -- time in (HH:)MM:SS format
    """
    h = 0
    try:
        h, m, s = [int(x) for x in time.split(':')]
    except ValueError:
        m, s = [int(x) for x in time.split(':')]
    secs = h*3600 + m*60 + s
    return secs


def GetNets(results, column=4):
    """Extract the net column and return the time in minutes."""
    nets = []
    for t in results:
        pace = t[column].translate(None, '*')
        secs = ConvertTimeToSeconds(pace)
        nets.append(secs/60.0)
    return nets


def Percentile(scores, percentile_rank):
    """Returns the score at the given percentile_rank
    
    Arguments:
    scores -- list of scores
    percentile_rank -- the percentile rank to find
    """
    num_smallest = int(len(scores) * percentile_rank / 100)
    return heapq.nsmallest(num_smallest, scores)[-1]
        

def PercentileRank(scores, your_score):
    """Returns the percentile rank of your_score within the population of 
    scores.
    
    Arguments:
    scores -- list of scores
    your_score -- the score being ranked
    """
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1
    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank


def PartitionDivisions(relay_results):
    """Returns result lists of several relay divisions.
    
    Arguments:
    relay_results -- list of relay result tuples
    """
    m4049 = []
    m5059 = []
    f2039 = []
    for result in relay_results:
        div = result[2]
        if div == "M4049":
            m4049.append(result)
        elif div == "M5059":
            m5059.append(result)
        elif div == "F2039":
            f2039.append(result)
    return m4049, m5059, f2039


def ProcessWeights(*tables):
    """Adds a weight field (in ounces) to a Pregnancy object
    
    Arguments:
    tables -- A list of Table objects
    """
    for table in tables:
        table.weights_oz = RecordWeightsAsList(table)
    
    
def RecordWeightsAsList(table):
    """Returns an array of all pregnancy birth weights in ounces typed as 
    floats.
    
    Arguments:
    table -- A Pregnancy table
    """
    weights_oz = []
    for p in table.records:
        # Dynamic types, ftw?
        lb = 0
        if p.birthwgt_lb != 'NA':
            lb = float(p.birthwgt_lb)
        oz = 0
        if p.birthwgt_oz != 'NA':
            oz = float(p.birthwgt_oz)
            
        # Trim invalid lb and oz measurements
        if lb < 50 and oz <= 16:
            weights_oz.append(lb * 16 + oz)
    return weights_oz


def StuObsPmf(d):
    """Returns a PMF of student class size observations.
    
    Arguments:
    d -- dictionary of class size:count
    """
    
    cl_size_obs = dict.fromkeys(d, 0)
    for sz, cnt in d.iteritems():
        freq = sz * cnt
        cl_size_obs[sz] = freq
    obs_hist = Pmf.MakeHistFromDict(cl_size_obs)
    obs_pmf = Pmf.MakePmfFromHist(obs_hist)
    return obs_pmf


def UnbiasPmf(biased_pmf):
    """Returns an unbiased PMF of student class sizes.
    
    Arguments:
    biased_pmf -- probability mass function of observations affected by 
                  oversampling bias
    """
    unbiased_pmf = biased_pmf.Copy()
    for sz, prob in unbiased_pmf.Items():
        unbiased_pmf.Mult(sz, 1.0 / sz)
    unbiased_pmf.Normalize()
    return unbiased_pmf
        

def main():
    """ Execute various exercises from chapter 3 of "Think Stats."
    """
    cl_size_counts = {7:8, 12:8, 17:14, 22: 4, 27:6, 32:12, 37:8, 42:3, 47:2}
    
    # Exercise 3.1
    # Internal Pmf.Normalize alters dict object, use a copy
    cl_size_pmf = Pmf.MakePmfFromDict(cl_size_counts.copy()) 
    print "Mean from the dean's perspective", cl_size_pmf.Mean()
    
    # Sample 500 students
    cl_size_obs_pmf = StuObsPmf(cl_size_counts)
    print "Mean from student observations", cl_size_obs_pmf.Mean()
    
    # Unbias the observed sample
    cl_size_obs_unbias_pmf = UnbiasPmf(cl_size_obs_pmf)
    print "Mean from unbiased student observations", cl_size_obs_unbias_pmf.Mean()
    
    
    # Exercise 3.2
    # ...maybe later
    
    
    # Exercise 3.3 and 3.4
    scores = [55, 66, 77, 88, 99]
    your_score = 88
    percentile_rank = PercentileRank(scores, your_score)
    print "Percentile rank", percentile_rank
    the_score = Percentile(scores, percentile_rank)
    print "Score found using percentile rank", the_score
    
    
    # Exercise 3.5, commented out to spare coolrunning.com
    relay_results = relay.ReadResults()
    speeds = relay.GetSpeeds(relay_results)
    # cdf = Cdf.MakeCdfFromList(speeds, 'speeds')
    # myplot.Cdf(cdf)
    # myplot.Show(title='CDF of running speed',
    #            xlabel='speed (mph)',
    #            ylabel='percentile')
    
    
    # Exercise 3.6
    table, firsts, others = first.MakeTables()
    first.ProcessTables(firsts, others)
    ProcessWeights(firsts, others)
    firsts_wgt_cdf = Cdf.MakeCdfFromList(firsts.weights_oz, 'firsts_wgt')
    for w in others.weights_oz:
        if w > 300:
            print w
    others_wgt_cdf = Cdf.MakeCdfFromList(others.weights_oz, 'others_wgt')
    print "Percentile of 5lb, 13oz baby", firsts_wgt_cdf.Prob(93.0)
    # myplot.Cdf(firsts_wgt_cdf)
    # myplot.Cdf(others_wgt_cdf)
    # myplot.Show(title="CDF of birth weights",
    #             xlabel="weight (ounces)",
    #             yplabel="percentile")
    
    
    # Exercise 3.7
    # The birth weight CDF for an academic class would look more like the 
    # 'others' birth weight CDF since 'others' would be oversampled in any 
    # population. This was demonstrated by firsts.n and otheres.n in earlier 
    # chapters. I would expect more than half to be over the median birth 
    # weight due to this skew. The curve would be flattened due to this skew.
    
    
    # Exercise 3.8
    m4049, m5059, f2039 = PartitionDivisions(relay_results)
    m4049_cdf = Cdf.MakeCdfFromList(GetNets(m4049), "M4049")
    m5059_cdf = Cdf.MakeCdfFromList(GetNets(m5059), "M5059")
    f2039_cdf = Cdf.MakeCdfFromList(GetNets(f2039), "F2039")
    allen_mins = ConvertTimeToSeconds("42:44") / 60.0
    print "Allen's time", allen_mins, "minutes"
    allen_percentile = m4049_cdf.Prob(allen_mins) * 100
    print "Allen's original percentile", allen_percentile
    print "Allen's 50-59 target time", m5059_cdf.Percentile(allen_percentile),\
          "minutes"
    print "Rival's target time", f2039_cdf.Percentile(allen_percentile),\
          "minutes"

if __name__ == "__main__":
    main()
