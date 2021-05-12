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
	with open("reflexiveAcrossObjRel_data.tsv", "w") as out_file:
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
	# Reflexive across object relative clause (singular noun + faulty inflection)
	reflOb = """ 
	S -> NP RelCl VP ANPHRs ref
	S -> NP RelCl VP ANPHRp ref
	NP -> Detsg Nsg
	RelCl -> sconj Detpl Nplur Vp
	VP -> Vpart
	Detsg -> 'in'
	Nsg -> 'man' | 'heit' | 'jonge' | 'kening'
	sconj -> "dêr't"
	Detpl -> 'de'
	Nplur -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	Vp -> 'fan hâlde' | 'bewûnderje' | 'haatsje'
	Vpart -> 'ferwûne' | 'lokwinsket' | 'ferlegen' | 'ferklaaide' | 'hatet'
	ANPHRs -> 'him'
	ANPHRp -> 'har'
	ref -> 'sels'
	"""

	# Singular Nonce
	reflObN = """ 
	S -> NP RelCl VP ANPHRs ref
	S -> NP RelCl VP ANPHRp ref
	NP -> Detsg Nsg
	RelCl -> sconj Detpl Nplur Vp
	VP -> Vpart
	Detsg -> 'in'
	sconj -> "dêr't"
	Detpl -> 'de'
	Vpart -> 'ferwûne' | 'lokwinsket' | 'ferlegen' | 'ferklaaide' | 'hatet'
	ANPHRs -> 'him'
	ANPHRp -> 'har'
	ref -> 'sels'
	"""

	# Optional both singular
	reflObsg2 = """ 
	S -> NP RelCl VP ANPHRs ref
	S -> NP RelCl VP ANPHRp ref
	NP -> Detsg Nsg
	RelCl -> sconj Detsg Nsing Vs
	VP -> Vpart
	Detsg -> 'in'
	Nsg -> 'man' | 'heit' | 'jonge' | 'kening'
	sconj -> "dêr't"
	Detpl -> 'de'
	Nsing -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Vs -> 'fan hâldt' | 'bewûnderet' | 'hatet'
	Vpart -> 'ferwûne' | 'lokwinsket' | 'ferlegen' | 'ferklaaide' | 'hatet'
	ANPHRs -> 'him'
	ANPHRp -> 'har'
	ref -> 'sels'
	"""

	# Reflexive across object relative clause (plural + faulty inflection)
	reflObpl = """ 
	S -> NP RelCl VP ANPHRp ref
	S -> NP RelCl VP ANPHRs ref
	NP -> Detpl Npl
	RelCl -> sconj Det Nsg Vs
	VP -> Vpart
	Detpl -> 'de'
	Npl -> 'manlju' | 'heiten' | 'jonges' | 'keningen'
	sconj -> "dêr't"
	Det -> 'in'
	Nsg -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Vs -> 'fan hâldt' | 'bewûnderet' | 'hatet'
	Vpart -> 'ferwûnen' | 'lokwinsken' | 'ferlegen' | 'ferklaaiden' | 'hate'
	ANPHRp -> 'har'
	ANPHRs -> 'him'
	ref -> 'sels'
	"""

	# Plural Nonce
	reflObplN = """ 
	S -> NP RelCl VP ANPHRp ref
	S -> NP RelCl VP ANPHRs ref
	NP -> Detpl Npl
	RelCl -> sconj Det Nsg Vs
	VP -> Vpart
	Detpl -> 'de'
	sconj -> "dêr't"
	Det -> 'in'
	Vpart -> 'ferwûnen' | 'lokwinsken' | 'ferlegen' | 'ferklaaiden' | 'hate'
	ANPHRp -> 'har'
	ANPHRs -> 'him'
	ref -> 'sels'
	"""

	#Optional both plural
	reflObpl2 = """ 
	S -> NP RelCl VP ANPHRp ref
	S -> NP RelCl VP ANPHRs ref
	NP -> Detpl Npl
	RelCl -> sconj Detpl Nplur Vp
	VP -> Vpart
	Detpl -> 'de'
	Npl -> 'manlju' | 'heiten' | 'jonges' | 'keningen'
	sconj -> "dêr't"
	Det -> 'in'
	Nplur -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	Vp -> 'fan hâlde' | 'bewûnderje' | 'haatsje'
	Vpart -> 'ferwûnen' | 'lokwinsken' | 'ferlegen' | 'ferklaaiden' | 'hate'
	ANPHRp -> 'har'
	ANPHRs -> 'him'
	ref -> 'sels'
	"""

	sg, sgfl = createLists(reflOb)
	ror_sing = list(zip(sg, sgfl))
	pl, plfl = createLists(reflObpl)
	ror_plur = list(zip(pl, plfl))

	sg2, sgfl2 = createLists(reflObsg2)
	ror_sing2 = list(zip(sg2, sgfl2))
	pl2, plfl2 = createLists(reflObpl2)
	ror_plur2 = list(zip(pl2, plfl2))

# Get random words
	NounSing = get_words("randomWords/acrossObjRel/reflObjSingNoun0205.csv")
	NounPlur = get_words("randomWords/acrossObjRel/reflObjPlurNoun0205.csv")
	VerbSing = get_words("randomWords/acrossObjRel/reflObjSingVerb0205.csv")
	VerbPlur = get_words("randomWords/acrossObjRel/reflObjPlurVerb0205.csv")

	noncesing = addToGram(NounSing, reflObN, "Nsg")
	noncesing = addToGram(NounPlur, noncesing, "Nplur")
	noncesing = addToGram(VerbPlur, noncesing, "Vp")
	sgn, sgnfl = createLists(noncesing)
	ror_singNonce = list(zip(sgn, sgnfl))


	nonceplur = addToGram(NounPlur, reflObplN, "Npl")
	nonceplur = addToGram(NounSing, nonceplur, "Nsg")
	nonceplur = addToGram(VerbSing, nonceplur, "Vs")
	pln, plfln = createLists(nonceplur)
	ror_plurNonce = list(zip(pln, plfln))

	writeTSV(ror_sing, ror_plur, ror_singNonce, ror_plurNonce, ror_sing2, ror_plur2, "Reflexive_AOR", "ror_sg", "ror_pl", "ror_sgN", "ror_plN", "ror_sg2", "ror_pl2")
if __name__ == '__main__':
	main()