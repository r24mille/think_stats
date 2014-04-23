'''
Created on Apr 21, 2014

@author: Reid Miller
'''
import collections
import gzip
import math
import numpy
import os
import random
import re

from chapter_four import erf
from chapter_one import first_ans as first
from chapter_three import Cdf
from chapter_two import Pmf
from chapter_two import myplot
from chapter_two import thinkstats


def paretovariate(alpha, xm):
    """Wrapper function around random.paretovariate that returns values from a
    two-parameter Pareto distribution.

    Arguments:
    alpha -- the shape parameter
    xm -- the minimum possible value of X (ie. "x sub m")
    """
    pareto_v = random.paretovariate(alpha)
    pareto_v = xm * pareto_v
    return pareto_v


def Sample(n=6, mu=0, sigma=1):
    """Returns a list of n samples from a normal distribution with mean mu
    and standard deviation sigma.

    Arguments:
    n -- list size
    mu -- mean of normal distribution
    sigma -- standard deviation of normal distribution
    """
    sample = []
    for i in range(0, n):
        sample.append(random.normalvariate(mu=0, sigma=1))
    sample.sort()
    return sample

def Samples(k=1000):
    """Calls Sample k times to create a list of lists

    Arguments:
    k -- number of calls to Sample
    """
    samples = []
    for i in range(0, k):
        samples.append(Sample(n=6))
    return samples

def main():
    """Main method for executing exercises from chapter 4"""
    # Exercise 4.1
    exponential_dist = []
    mu = 32.6
    for i in range (0, 44):
        exponential_dist.append(random.expovariate(1.0 / mu))
    exp_dist_cdf = Cdf.MakeCdfFromList(exponential_dist,
                                       name="exponential_dist")
    # scale = myplot.Cdf(exp_dist_cdf, complement=True, xscale="linear", yscale="log")
    # myplot.Show(title="Complement of an Exponential Distribution Sample", yscale=scale['yscale'])

    # Exercise 4.2
    # No class :(
    
    # Exercise 4.3
    pareto_dist = []
    alpha = 2
    xm = 5
    for i in range (0, 1000):
        pareto_dist.append(paretovariate(alpha, xm))
    pareto_dist_cdf = Cdf.MakeCdfFromList(pareto_dist, name="pareto_dist")
    # scale = myplot.Cdf(pareto_dist_cdf, complement=True, transform="pareto")
    # myplot.Show(title="Complement of Pareto Distribution Sample", 
    #             yscale=scale["yscale"], xscale=scale["xscale"])
    
    # Exercise 4.4
    pareto_heights = []
    alpha = 1.7
    xm = 100
    for i in range (0, 6000):
        pareto_heights.append(paretovariate(alpha, xm))
    pareto_dist_cdf = Cdf.MakeCdfFromList(pareto_heights,
                                          name="pareto_heights")
    print "Mean height in Pareto World", pareto_dist_cdf.Mean()
    print "Max height in Pareto World", max(pareto_dist_cdf.Values())
    
    # Exercise 4.5
    filename = os.path.join(".", "kjvdat.txt.gz")  # King James Bible
    fp = gzip.open(filename)
    counts = collections.Counter()
    words_re = re.compile("(\w[\w']*)")  # Simple word-split regex
    # Iterate over lines in text file
    for i, line in enumerate(fp):
        if i == None:
            break
        counts.update(words_re.findall(line.lower()))
    fp.close()
    bible_words_cdf = Cdf.MakeCdfFromList(counts.values(),
                                          name="bible_words_cdf")
    # scale = myplot.Cdf(bible_words_cdf, complement=True, transform="pareto")
    # myplot.Show(title="Complement of Word Occurences in KJV Bible",
    #             yscale=scale["yscale"], xscale=scale["xscale"])
    xs, ps = bible_words_cdf.Render()
    ps = [1.0 - p for p in ps]  # complement
    del xs[-1]
    del ps[-1]
    slope, intercept = numpy.polyfit(numpy.log(xs), numpy.log(ps), 1)
    print "Slope", slope
    print "Intercept", intercept
    
    # Exercise 4.6
    weibull_dist = []
    for i in range(0, 1000):
        weibull_dist.append(random.weibullvariate(alpha=1, beta=1))
    weibull_dist_cdf = Cdf.MakeCdfFromList(weibull_dist,
                                       name="weibull_dist")
    # scale = myplot.Cdf(weibull_dist_cdf, complement=True, yscale="log")
    # myplot.Show(title="Weibull Distribution Sample", yscale=scale["yscale"])
    
    # Exercise 4.7
    iqs = [115, 130, 145]
    for iq in iqs:
        wechsler_p = erf.NormalCdf(x=iq, mu=100, sigma=15)
        print "Percentile of IQ=", iq, "is", wechsler_p * 100.0
    genius_p = erf.NormalCdf(x=190, mu=100, sigma=15)
    print "Number of geniuses in the world", 6000000000 * (1.0 - genius_p)
    
    # Exercise 4.8
    table, firsts, others = first.MakeTables()
    first.Process(table)
    lengths_cdf = Cdf.MakeCdfFromList(table.lengths, name="gestation_lengths")
    len_var = thinkstats.Var(table.lengths)
    len_sigma = math.sqrt(len_var)
    model_lengths = []
    for i in range(0, 1000):
        model_lengths.append(random.gauss(mu=table.mu, sigma=len_sigma))
    normal_cdf = Cdf.MakeCdfFromList(model_lengths, name="gaussian_model")
    # myplot.Cdf(lengths_cdf)
    # myplot.Cdf(normal_cdf)
    # myplot.Show(title="Empirical and Modeled Gestation Lengths")
    
    # Exercise 4.9
    samples = Samples(k=1000)
    z_samples = zip(*samples)
    # print "zipped samples", z_samples
    # for s in z_samples:
    #     print "s", s
    print "Zipped means", [ thinkstats.Mean(s) for s in z_samples ]

if __name__ == '__main__':
    main()
