#Adapted from https://github.com/yoavg/bert-syntax
import sys
from collections import *

files=[("ph","results_xlmmlm/prepPh_animate_resultsX.txt")]

by_model={}
by_model_sub={}
conditions=set()
subconditions=set()
for title,fname in files:
    lines = open(fname)
    results=defaultdict(Counter)
    subresults = defaultdict(Counter)
    by_model[title]=results
    by_model_sub[title]=subresults
    skipped = set()
    for line in lines:
        if line.startswith("Better speed"): continue
        if line.startswith("skipping"):
            skipped.add(line.split()[1])
            # Use next(lines) if you want results without the skipped items
            # next(lines)
            continue
        res,c1,c2,w1,w2,s = line.split(None, 5)
        conditions.add(c1)
        subconditions.add(c2)
        results[c1][res]+=1
        subresults[c2][res] +=1

print("skipped:",skipped)

print("condition & accuracy & count \\\\")
for cond in conditions:
    rb = by_model['ph'][cond]
    sb = "%.3f" % (rb['True']/(rb['True']+rb['False']))
    print(" & ".join(map(str,[cond, sb, sum(rb.values())])),"\\\\")


print("subcondition & accuracy & count \\\\")
for scond in subconditions:
    rbs = by_model_sub['ph'][scond]
    sbs = "%.2f" % (rbs['True']/(rbs['True']+rbs['False']))
    print(" & ".join(map(str,[scond, sbs, sum(rbs.values())])),"\\\\")   


