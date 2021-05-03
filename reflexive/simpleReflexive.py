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

def get_words(csvFile):
	df = pd.read_csv(csvFile, sep=",")
	list_of_words = df['word'].to_list()
	list_of_words.sort()
	return list_of_words


def addToGram(PROPNsing, Grammar, name):
	s = ""
	listOfpropn = []
	for propns in PROPNsing:
		s = name + " -> " + "'"+propns+"'"
		listOfpropn.append(s)

	props = '\n'.join(listOfpropn)
	gr = Grammar + "\n" + props

	return(gr)

def writeTSV(Sing, Plur, SingNonce, PlurNonce, mainName, S, P, SN, PN):
	with open("simpleRefl_data.tsv", "w") as out_file:
		tsv_output = csv.writer(out_file, delimiter='\t')

		# Write minimal pairs singular
		for it in Sing:
			start = [mainName, S]
			start.extend(it)
			tsv_output.writerow(start)
	
		# Write minimal pairs plural
		for i in Plur:
			stplu = [mainName, P]
			stplu.extend(i)
			tsv_output.writerow(stplu)

		# Write minimal pairs singular nonce
		for p in SingNonce:
			sinnonce = [mainName, SN]
			sinnonce.extend(p)
			tsv_output.writerow(sinnonce)

		# Write minimal pairs plural nonce
		for pp in PlurNonce:
			plunonce = [mainName, PN]
			plunonce.extend(pp)
			tsv_output.writerow(plunonce)

def main():
	# Simple reflexive (singular noun + faulty inflection)
	refl = """ 
	S -> NP VP ANPHRs ref
	S -> NP VP ANPHRp ref
	NP -> Det Nsi
	Det -> 'in'
	ANPHRs -> 'him'
	ANPHRp -> 'har'
	Nsi ->  'man' | 'heit' | 'jonge' | 'kening'
	VP -> 'ferwûne' | 'lokwinsket' | 'ferlegen' | 'ferklaaide' | 'hate'
	ref -> 'sels'
	"""

	# Simple Nonce
	reflns = """ 
	S -> NP VP ANPHRs ref
	S -> NP VP ANPHRp ref
	NP -> Det Nsi
	Det -> 'in'
	ANPHRs -> 'him'
	ANPHRp -> 'har'
	ref -> 'sels'
	"""

	# Simple reflexive (plural noun + faulty inflection)
	reflpl = """ 
	S -> NP VP ANPHRp ref
	S -> NP VP ANPHRs ref
	NP -> Det Np
	Det -> 'de'
	ANPHRs -> 'him'
	ANPHRp -> 'har'
	Np ->  'manlju' | 'heiten' | 'jonges' | 'keningen'
	VP -> 'ferwûnen' | 'lokwinsken' | 'ferlegen' | 'ferklaaiden' | 'hate'
	ref -> 'sels'
	"""


	# Plural Nonce
	reflplN = """ 
	S -> NP VP ANPHRp ref
	S -> NP VP ANPHRs ref
	NP -> Det Np
	Det -> 'de'
	ANPHRs -> 'him'
	ANPHRp -> 'har'
	ref -> 'sels'
	"""

	refl, relffl = createLists(refl)
	reflSing = list(zip(refl, relffl))
	refpl, refplfl = createLists(reflpl)
	refPlur = list(zip(refpl, refplfl))

	# Get random words
	NounSing = get_words("randomWords/simpleRefl/SimpRSingularNouns3004.csv")
	NounPlur = get_words("randomWords/simpleRefl/SimpRPluralNouns3004.csv")
	VerbsSing = get_words("randomWords/simpleRefl/SimpRSingularVerbs3004.csv")
	VerbsPlur = get_words("randomWords/simpleRefl/SimpRPluralVerbs3004.csv")

	noncesing = addToGram(NounSing, reflns, "Nsi")
	noncesing = addToGram(VerbsSing, noncesing, "VP")
	nonces, noncesfl = createLists(noncesing)
	nonceSing = list(zip(nonces, noncesfl))

	nonceplur = addToGram(NounPlur, reflplN, "Np")
	nonceplur = addToGram(VerbsPlur, nonceplur, "VP")
	noncep, noncepfl = createLists(nonceplur)
	noncePlur = list(zip(noncep, noncepfl))
	
	writeTSV(reflSing, refPlur, nonceSing, noncePlur, "SimpleReflexive", "siRefsg", "siRefpl", "siRefsgN", "siRefplN")

if __name__ == '__main__':
	main()