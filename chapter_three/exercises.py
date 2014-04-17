'''
Created on Apr 17, 2014

@author: r24mille
'''
from chapter_two import Pmf
from chapter_two.exercises import PmfMean
import matplotlib.pyplot as pyplot


def main():
    """ Execute various exercises from chapter 3 of "Think Stats."
    """
    cl_size_counts = {7:8, 12:8, 17:14, 22: 4, 27:6, 32:12, 37:8, 42:3, 47:2}
    
    # Exercise 3.1
    cl_size_pmf = Pmf.MakePmfFromDict(cl_size_counts)
    dean_mean = PmfMean(cl_size_pmf)
    print "Mean from the dean's perspective", dean_mean
    
    # Sample 500 students
    cl_size_weighted = dict.fromkeys(cl_size_counts, 0)
    for sz, cnt in cl_size_pmf.Items():
        weight = sz * cnt
        cl_size_weighted[sz] = weight
    cl_size_weighted_pmf = Pmf.MakePmfFromDict(cl_size_weighted)
    student_mean = PmfMean(cl_size_weighted_pmf)
    print "Mean from students' perspectives", student_mean
    vals, probs = cl_size_weighted_pmf.Render()
    rectangles = pyplot.bar(vals, probs)
    pyplot.show()

if __name__ == "__main__":
    main()
