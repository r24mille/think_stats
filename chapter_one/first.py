'''
Created on Apr 15, 2014

@author: r24mille
'''

# Initial code reccomended in Excersize 1.3
import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

# Count the number of live births, outcome=1 is a live birth
numbirths = 0;
for record in table.records:
    if record.outcome == 1:
        numbirths += 1
print 'Number of live births', numbirths

# Modify the loop (though I'm creating a new loop) to partition live birth 
# records into two groups. One for first babies and one for others. The 
# birthord code for a first child is 1.
firstbirths = []
otherbirths = []
for record in table.records:
    if record.outcome == 1:
        if record.birthord == 1:
            firstbirths.append(record)
        else:
            otherbirths.append(record)
print 'Number of first births', len(firstbirths)
print 'Number of non-first births', len(otherbirths)

# Compute the average pregnancy length (in weeks) for first births and others.
# prglength is the integer duration of the pregnancy in weeks.
total_first_preg_len = 0
total_other_preg_len = 0

for record in firstbirths:
    total_first_preg_len += record.prglength
avg_first_preg_len = float(total_first_preg_len) / len(firstbirths)
print 'Average pregnancy length for first births', avg_first_preg_len

for record in otherbirths:
    total_other_preg_len += record.prglength
avg_other_preg_len = float(total_other_preg_len) / len(otherbirths)
print 'Average pregnancy length for other births', avg_other_preg_len

print 'Difference between pregnancy length of first births to others', \
      (avg_first_preg_len - avg_other_preg_len), 'weeks, aka', \
      ((avg_first_preg_len - avg_other_preg_len) * 7), 'days.'
