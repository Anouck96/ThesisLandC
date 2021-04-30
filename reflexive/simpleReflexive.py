from nltk import CFG
from nltk.parse.generate import generate
import pandas as pd
import csv

def createLists(cfgString):
	PairsList = []
	l = CFG.fromstring(cfgString)
	for sent in generate(l):
		new = (' '.join(sent))
		PairsList.append(new)
	length = len(PairsList)
	middle_index = length//2
	correctList = PairsList[:middle_index]
	incorrectList = PairsList[middle_index:]
	return correctList, incorrectList

def main():
	# Simple reflexive (singular noun + faulty inflection)
	refl = """ 
	S -> NP VP ANPHRs
	S -> NP VP ANPHRp
	NP -> Det Nsi
	Det -> 'in'
	ANPHRs -> 'him'
	ANPHRp -> 'har'
	Nsi ->  'man' | 'heit' | 'jonge' | 'kening'
	VP -> 'ferwûne' | 'lokwinsket' | 'ferlegen' | 'ferklaaide' | 'hate'
	"""

	# Simple reflexive (plural noun + faulty inflection)
	reflpl = """ 
	S -> NP VP ANPHRp
	S -> NP VP ANPHRs
	NP -> Det Np
	Det -> 'de'
	ANPHRs -> 'him'
	ANPHRp -> 'har'
	Np ->  'manlju' | 'heiten' | 'jonges' | 'keningen'
	VP -> 'ferwûnen' | 'lokwinsken' | 'ferlegen' | 'ferklaaiden' | 'hate'
	"""

	refl, relffl = createLists(refl)
	reflSing = list(zip(refl, relffl))
	refpl, refplfl = createLists(reflpl)
	refPlur = list(zip(refpl, refplfl))


if __name__ == '__main__':
	main()
