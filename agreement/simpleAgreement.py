from nltk import CFG
from nltk.parse.generate import generate
import pandas as pd

def createLists(cfgString):
	PairsList = []
	l = CFG.fromstring(cfgString)
	for sent in generate(l):
		new = (' '.join(sent))
		PairsList.append(new)

	return PairsList
def main():

# Singular Noun simple agreement
	simpAgrSing = """
	S -> NP VP PUNCT
	VP -> V
	NP -> Det N
	NP -> Propn
	Det -> 'in'
	N -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	V -> 'hat' | 'giet' | 'komt' | 'freget' | 'stiet' | 'rûn' | 'sit' | 'praat'
	PUNCT -> '.'
	"""

# Singular Noun with faulty plural verb
	simpAgrSingFault = """ 
	S -> NP VP PUNCT
	VP -> V
	NP -> Det N
	NP -> Propn
	Det -> 'in'
	N -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	V -> 'hawwe' | 'geane' | 'komme' | 'freegje' | 'steane' | 'rinne' |'sitte' | 'prate'
	PUNCT -> '.'
	"""

# Plural Noun simple agreement
	simpAgrPlCor = """ 
	S -> NP VP PUNCT
	VP -> V
	NP -> Det N
	NP -> Propn
	Det -> 'de'
	N -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	V -> 'hawwe' | 'geane' | 'komme' | 'freegje' | 'steane' | 'rinne' |'sitte' | 'prate'
	PUNCT -> '.'
	"""
# Plural Noun with faulty singular verb
	simpAgrPlFault = """
	S -> NP VP PUNCT
	VP -> V
	NP -> Det N
	NP -> Propn
	Det -> 'de'
	N -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	V -> 'hat' | 'giet' | 'komt' | 'freget' | 'stiet' | 'rûn' | 'sit' | 'praat'
	PUNCT -> '.'
	"""

	MinPairsSingCor = createLists(simpAgrSing)
	MinPairsSingFa = createLists(simpAgrSingFault)
	MinPairsPlurCor = createLists(simpAgrPlCor)
	MinPairsPlurFa = createLists(simpAgrPlFault)

	SimpAgrSingular = list(zip(MinPairsSingCor, MinPairsSingFa))
	print(SimpAgrSingular)

	SimpAgrPlural = list(zip(MinPairsPlurCor, MinPairsPlurFa))
	print(SimpAgrPlural)

if __name__ == '__main__':
	main()