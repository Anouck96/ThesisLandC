# Code adapted from https://github.com/yoavg/bert-syntax
from transformers import BertTokenizer
import torch
from transformers import pipeline
import sys
import csv

model_name = 'bert-large-multilingual-uncased'
if 'base' in sys.argv: model_name = 'bert-base-multilingual-uncased'
print("using model:",model_name,file=sys.stderr)
tokenizer=BertTokenizer.from_pretrained(model_name)
mbert = pipeline('fill-mask', model=model_name)

def probe(Sentence,Targets) :
    probs = []
    cor = Targets[0]
    for res in mbert(Sentence,targets=Targets) :
        probs.append((cor, res['token_str'], res['score']))
    return probs

def get_probs_for_words(sent,w1,w2):
    pre,target,post=sent.split('***')
    if 'mask' in target.lower():
        target=['[MASK]']
    else:
        target=tokenizer.tokenize(target)

    tokens=['[CLS]']+tokenizer.tokenize(pre)
    target_idx=len(tokens)
    tokens+=target+tokenizer.tokenize(post)+['[SEP]']

    input_ids=tokenizer.convert_tokens_to_ids(tokens)
    try:
        word_ids=tokenizer.convert_tokens_to_ids([w1,w2])
        sent = sent.replace("***mask***", "[MASK]")
        probs = probe(sent, [w1, w2])
        return(probs)
    except KeyError:
        print("skipping",w1,w2,"bad wins")
        return None


from collections import Counter
def load_marvin():
    # Creates the sentences with masks and gets minimal differences (words)
    cc = Counter()
    out = []
    for line in open("testcases/simpagr_data.tsv"):
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
