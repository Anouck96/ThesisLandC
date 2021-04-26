#Adapted from https://github.com/yoavg/bert-syntax
import sys
from collections import *

files=[("base","results/outsimpagr.txt")]

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
            next(lines)
            continue
        res,c1,c2,w1,w2,s = line.split(None, 5)
     #   c1 = c1.replace("inanim","anim")
        conditions.add(c1)
        subconditions.add(c2)
        results[c1][res]+=1
        subresults[c2][res] +=1

print(subresults)
print("skipped:",skipped)

print("condition & base & count \\\\")
for cond in conditions:
    rb = by_model['base'][cond]
    # rl = by_model['large'][cond]
    sb = "%.3f" % (rb['True']/(rb['True']+rb['False']))
    # sl = "%.2f" % (rl['True']/(rl['True']+rl['False']))
    print(" & ".join(map(str,[cond, sb, sum(rb.values())])),"\\\\")


print("subcondition & base & count \\\\")
for scond in subconditions:
    rbs = by_model_sub['base'][scond]
    # rl = by_model['large'][cond]
    sbs = "%.2f" % (rbs['True']/(rbs['True']+rbs['False']))
    # sl = "%.2f" % (rl['True']/(rl['True']+rl['False']))
    print(" & ".join(map(str,[scond, sbs, sum(rbs.values())])),"\\\\")   


