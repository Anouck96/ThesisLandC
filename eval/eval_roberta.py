# Code adapted from https://github.com/yoavg/bert-syntax
from transformers import XLMRobertaTokenizer
import torch
from transformers import pipeline
import sys
import csv

model_name = 'xlm-roberta-large'
if 'base' in sys.argv: model_name = 'xlm-roberta-base'
print("using model:",model_name,file=sys.stderr)
tokenizer=XLMRobertaTokenizer.from_pretrained(model_name)
mbert = pipeline('fill-mask', model=model_name)

def probe(Sentence,Targets) :
	# Finds probabilities for the two words
    probs = []
    cor = Targets[0]
    for res in mbert(Sentence,targets=Targets) :
        probs.append((cor, res['token_str'], res['score']))
    return probs

def get_probs_for_words(sent,w1,w2):
	# Checks if the words are in the vocab; returns probabilities
    if  len(tokenizer.tokenize(w1)) == 1 and len(tokenizer.tokenize(w2)) == 1:
        word_ids=tokenizer.convert_tokens_to_ids([w1,w2])
        sent = sent.capitalize()
        sent = sent.replace("***mask***", "<mask>")
        probs = probe(sent, [w1, w2])
        return(probs)
    else:
        print("skipping",w1,w2,"bad wins")
        return("NA")


from collections import Counter
def load_marvin():
    # Creates the sentences with masks and gets minimal differences (words)
    cc = Counter()
    out = []
    for line in open("data/subrelclause_data.tsv"):
        case = line.strip().split("\t")
        cc[case[1]]+=1
        g,ug = case[-2],case[-1]
        g = g.split()
        ug = ug.split()
        assert(len(g)==len(ug)),(g,ug)
        diffs = [i for i,pair in enumerate(zip(g,ug)) if pair[0]!=pair[1]]
        if (len(diffs)!=1):
            continue    
        assert(len(diffs)==1),diffs
        gv=g[diffs[0]]   # good
        ugv=ug[diffs[0]] # bad
        g[diffs[0]]="***mask***"
        g.append(".")
        out.append((case[0],case[1]," ".join(g),gv,ugv))
    return out

def main():
    o = load_marvin()
    print(len(o),file=sys.stderr)   #Check number of items
    from collections import defaultdict
    for i,(case,tp,s,g,b) in enumerate(o):
        ps = get_probs_for_words(s,g,b)
        s = s.capitalize()
        if ps == "NA":
        	print(f"False {case} {tp} {g} {b} {s}")
        else:
            correct = ps[0][0]
            if ps[0][1] == correct:
                correctScore = ps[0][2]
            elif ps[1][1] == correct:
                correctScore = ps[1][2]
            if ps[0][1] != correct:
                incorrectScore = ps[0][2]
            elif ps[1][1] != correct:
                incorrectScore = ps[1][2]

            if correctScore > incorrectScore:
                 print(f"True {case} {tp} {g} {b} {s}" )
            else:
                 print(f"False {case} {tp} {g} {b} {s}")

if __name__ == '__main__':
    main()



