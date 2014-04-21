'''
Created on Apr 17, 2014

@author: r24mille
'''
from chapter_two import Pmf
from chapter_two.exercises import PmfMean
import matplotlib.pyplot as pyplot


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
    
    
    vals, probs = cl_size_obs_unbias_pmf.Render()
    rectangles = pyplot.bar(vals, probs)
    pyplot.show()

if __name__ == "__main__":
    main()
