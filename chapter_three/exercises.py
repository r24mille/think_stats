'''
Created on Apr 17, 2014

@author: r24mille
'''
from chapter_two import Pmf
from chapter_two.exercises import PmfMean


def main():
    """ Execute various exercises from chapter 3 of "Think Stats."
    """
    cl_size_counts = {7:8, 12:8, 17:14, 22: 4, 27:6, 32:12, 37:8, 42:3, 47:2}
    
    #Exercise 3.1
    class_size_pmf = Pmf.MakePmfFromDict(cl_size_counts)
    dean_mean = PmfMean(class_size_pmf)
    print "Mean from the dean's perspective", dean_mean
    

if __name__ == "__main__":
    main()