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

def writeTSV(sing, plu, singNonce, pluNonce, sing2, plu2, mainName, s, p, sn, pn, ss, pp):
	with open("reflSentComp_data.tsv", "w") as out_file:
		tsv_output = csv.writer(out_file, delimiter='\t')

		# Write minimal pairs singular
		for it in sing:
			start = [mainName, s]
			start.extend(it)
			tsv_output.writerow(start)
	
		# Write minimal pairs plural
		for i in plu:
			stplu = [mainName, p]
			stplu.extend(i)
			tsv_output.writerow(stplu)

		# Write minimal pairs singular nonce
		for p in singNonce:
			sinnonce = [mainName, sn]
			sinnonce.extend(p)
			tsv_output.writerow(sinnonce)

		# Write minimal pairs plural nonce
		for q in pluNonce:
			plunonce = [mainName, pn]
			plunonce.extend(q)
			tsv_output.writerow(plunonce)

		# Write minimal pairs singular switched
		for s in sing2:
			st = [mainName, ss]
			st.extend(s)
			tsv_output.writerow(st)

		# Write minimal pairs singular switched
		for e in plu2:
			swp = [mainName, pp]
			swp.extend(e)
			tsv_output.writerow(swp)

def main():

	# Reflexive sentential complement (singular noun + faulty inflection)
	sentRefl = """ 
	S -> NP VP Comp
	S -> NP VP Compfl
	NP -> Detp Npl
	VP -> Vpl
	Comp -> sconj Det Nsing ANPHRs ref Vpart
	Compfl -> sconj Det Nsing ANPHRp ref Vpart
	Detp -> 'de'
	Npl -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	Vpl -> 'seinen' | 'seagen' | 'tochten' | 'wisten'
	sconj -> 'dat'
	Det -> 'in'
	Nsing -> 'man' | 'heit' | 'jonge' | 'kening'
	ANPHRs -> 'him'
	ANPHRp -> 'har'
	Vpart -> 'ferwûne' | 'lokwinsket' | 'ferlegen' | 'ferklaaide' | 'hatet'
	ref -> 'sels'
	"""

	# Reflexive sentential complement (singular noun + faulty inflection) - NONCE version
	sentReflNon = """ 
	S -> NP VP Comp
	S -> NP VP Compfl
	NP -> Detp Npl
	VP -> Vpl
	Comp -> sconj Det Nsing ANPHRs ref aux Vpart
	Compfl -> sconj Det Nsing ANPHRp ref aux Vpart
	Detp -> 'de'
	sconj -> 'dat'
	Det -> 'in'
	ANPHRs -> 'him'
	ANPHRp -> 'har'
	Vpart -> 'ferwûne' | 'lokwinsket' | 'ferlegen' | 'ferklaaide' | 'hatet'
	ref -> 'sels'
	"""

	# Optional both singular
	sentReflSG2 = """ 
	S -> NP VP Comp
	S -> NP VP Compfl
	NP -> Det Ns
	VP -> Vsg
	Comp -> sconj Det Nsing ANPHRs ref aux Vpart
	Compfl -> sconj Det Nsing ANPHRp ref aux Vpart
	Detp -> 'de'
	Ns -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Vsg -> 'sei' | 'seach' | 'tocht' | 'wist'
	sconj -> 'dat'
	Det -> 'in'
	Nsing -> 'man' | 'heit' | 'jonge' | 'kening'
	ANPHRs -> 'him'
	ANPHRp -> 'har'
	Vpart -> 'ferwûne' | 'lokwinsket' | 'ferlegen' | 'ferklaaide' | 'hatet'
	ref -> 'sels'
	"""

	# Reflexive sentential complement (plural noun + faulty inflection)
	sentReflpl = """ 
	S -> NP VP Comp
	S -> NP VP Compfl
	NP -> Det Nsg
	VP -> Vsg
	Comp -> sconj Detpl Nplur ANPHRp ref Vpart
	Compfl -> sconj Detpl Nplur ANPHRs ref Vpart
	Det -> 'in'
	Nsg -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Vsg -> 'sei' | 'seach' | 'tocht' | 'wist'
	sconj -> 'dat'
	Detpl -> 'de'
	Nplur -> 'manlju' | 'heiten' | 'jonges' | 'keningen'
	ANPHRp -> 'har'
	ANPHRs -> 'him'
	Vpart -> 'ferwûnen' | 'lokwinsken' | 'ferlegen' | 'ferklaaiden' | 'hate'
	ref -> 'sels'
	"""
	# Reflexive sentential complement (plural noun + faulty inflection) - Nonce version
	sentReflplNon = """ 
	S -> NP VP Comp
	S -> NP VP Compfl
	NP -> Det Nsg
	VP -> Vsg
	Comp -> sconj Detpl Nplur ANPHRp ref Vpart
	Compfl -> sconj Detpl Nplur ANPHRs ref Vpart
	Det -> 'in'
	sconj -> 'dat'
	Detpl -> 'de'
	ANPHRp -> 'har'
	ANPHRs -> 'him'
	Vpart -> 'ferwûnen' | 'lokwinsken' | 'ferlegen' | 'ferklaaiden' | 'hate'
	ref -> 'sels'
	"""

	# Optional both plural
	sentReflPl2 = """ 
	S -> NP VP Comp
	S -> NP VP Compfl
	NP -> Detpl Np
	VP -> Vpl
	Comp -> sconj Detpl Nplur ANPHRp ref aux Vpart
	Compfl -> sconj Detpl Nplur ANPHRs ref aux Vpart
	Det -> 'in'
	Np -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	Vpl -> 'seinen' | 'seagen' | 'tochten' | 'wisten'
	sconj -> 'dat'
	Detpl -> 'de'
	Nplur -> 'manlju' | 'heiten' | 'jonges' | 'keningen'
	ANPHRp -> 'har'
	ANPHRs -> 'him'
	Vpart -> 'ferwûnen' | 'lokwinsken' | 'ferlegen' | 'ferklaaiden' | 'hate'
	ref -> 'sels'
	"""

	reSg, reSgFl = createLists(sentRefl)
	reflSentCompSg = list(zip(reSg, reSgFl))
	rePl, rePlFl = createLists(sentReflpl)
	reflSentCompPl = list(zip(rePl, rePlFl))
	reSg2, reSgFl2 = createLists(sentReflSG2)
	reflSentCompSg2 = list(zip(reSg2, reSgFl2))
	rePl2, rePlFL2 = createLists(sentReflPl2)
	reflSentCompPl2 = list(zip(rePl2, rePlFL2))

	# Get random words
	NounSing = get_words("randomWords/reflexSentComp/reflSentCompSingNoun0205.csv")
	NounPlur = get_words("randomWords/reflexSentComp/reflSentCompPlurNoun0205.csv")
	VerbsSing = get_words("randomWords/reflexSentComp/reflSentCompSingVerb0205.csv")
	VerbsPlur = get_words("randomWords/reflexSentComp/reflSentCompPlurVerb0205.csv")

	nonceSing = addToGram(NounPlur, sentReflNon, "Npl")
	nonceSing = addToGram(VerbsPlur, nonceSing, "Vpl")
	nonceSing = addToGram(NounSing, nonceSing, "Nsing")
	sgnon, sgnonFl = createLists(nonceSing)
	singNonce = list(zip(sgnon, sgnonFl))

	noncePlur = addToGram(NounSing, sentReflplNon, "Nsg")
	noncePlur = addToGram(VerbsSing, noncePlur, "Vsg")
	noncePlur = addToGram(NounPlur, noncePlur, "Nplur")
	plnon, plnonFl = createLists(noncePlur)
	pluNonce = list(zip(plnon, plnonFl))

	writeTSV(reflSentCompSg, reflSentCompPl, singNonce, pluNonce, reflSentCompSg2, reflSentCompPl2, "Refl_sentComp", "rsc_sing", "rsc_plur", "rsc_singN", "rsc_plurN", "rsc_sing2", "rsc_plur2")

if __name__ == '__main__':
	main()


