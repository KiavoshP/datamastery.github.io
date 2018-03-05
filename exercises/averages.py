import csv
import json
import statistics as stats
import sys

if __name__ == '__main__':
    averages = {}
    with open(sys.argv[1]) as fin:
        for r in csv.DictReader(fin):
            averages[r['Student']] = stats.mean([float(r['Exam 1']),
                                                 float(r['Exam 2']),
                                                 float(r['Exam 3'])])
    json.dump(averages, open(sys.argv[2], 'w'))
