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
	with open("npiacrossrel_animate_data.tsv", "w") as out_file:
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

# NPI PAST
	npiPAST = """
	S -> NP1 Rel VP
	S -> NP2 Rel VP
	NP1 -> neg N
	NP2 -> det N
	Rel -> sconj det N Vrel
	VP -> aux npi adj Vpartic
	neg -> 'gjin'
	det -> 'de'
	N -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	sconj -> "dy't"
	Vrel -> 'fan hâlde' | 'bewûnderje'
	aux -> 'benne'
	npi -> 'ea'
	adj -> 'populêr' | 'ferneamd' | 'earste' | 'goed' | 'moai'
	Vpartic -> 'west' """

# NPI PAST Nonce
	npiPASTN = """
	S -> NP1 Rel VP
	S -> NP2 Rel VP
	NP1 -> neg N
	NP2 -> det N
	Rel -> sconj det N Vrel
	VP -> aux npi adj Vpartic
	neg -> 'gjin'
	det -> 'de'
	sconj -> "dy't"
	aux -> 'benne'
	npi -> 'ea'
	Vpartic -> 'west' """


# NPI FUTURE
	npiFUT = """
	S -> NP1 Rel VP
	S -> NP2 Rel VP
	NP1 -> neg N
	NP2 -> det N
	Rel -> sconj det N Vrel
	VP -> aux npi adj Vpartic
	neg -> 'gjin'
	det -> 'de'
	N -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	sconj -> "dy't"
	Vrel -> 'fan hâlde' | 'bewûnderje'
	aux -> 'sille'
	npi -> 'ea'
	adj -> 'populêr' | 'ferneamd' | 'earste' | 'goed' | 'moai'
	Vpartic -> 'wêze' """


# NPI FUTURE Nonce
	npiFUTN = """
	S -> NP1 Rel VP
	S -> NP2 Rel VP
	NP1 -> neg N
	NP2 -> det N
	Rel -> sconj det N Vrel
	VP -> aux npi adj Vpartic
	neg -> 'gjin'
	det -> 'de'
	sconj -> "dy't"
	aux -> 'sille'
	npi -> 'ea'
	Vpartic -> 'wêze' """

# NPI (hoege)
	npiH = """
	S -> NP Rel aux npi VP
	S -> NP Rel aux adj VP
	NP -> det N
	Rel -> sconj det N Vrel
	VP -> adp V
	det -> 'de'
	N -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	sconj -> "dy't"
	Vrel -> 'fan hâlde' | 'bewûnderje'
	aux -> 'hoege'
	npi -> 'net'
	adj -> 'wol'
	adp -> 'te'
	V -> 'sizze' | 'wolle' | 'gean' | 'stean' """


# NPI (hoege) Nonce
	npiHN = """
	S -> NP Rel aux npi VP
	S -> NP Rel aux adj VP
	NP -> det N
	Rel -> sconj det N Vrel
	VP -> adp V
	det -> 'de'
	sconj -> "dy't"
	aux -> 'hoege'
	npi -> 'net'
	adj -> 'wol'
	adp -> 'te'
	"""

	npiP, npiPFl = createLists(npiPAST)
	ar_npiPast = list(zip(npiP, npiPFl))
	npiF, npiFFl = createLists(npiFUT)
	ar_npiFut = list(zip(npiF, npiFFl))
	npiH, npiHFl = createLists(npiH)
	ar_npiHoege = list(zip(npiH, npiHFl))

	# Get random words
	NounPlur = get_words("randomWords/npiARel/npiarPlurNoun0205.csv")
	VerbPlur = get_words("randomWords/npiARel/npiarPlurVerb0205.csv")
	ADJ = get_words("randomWords/npiARel/npiarADJ0205.csv")
	VerbInf = get_words("randomWords/npiARel/npiarInfVerb0205.csv")

	pastNonce = addToGram(NounPlur, npiPASTN, "N")
	pastNonce = addToGram(VerbPlur, pastNonce, "Vrel")
	pastNonce = addToGram(ADJ, pastNonce, "adj")

	futNonce = addToGram(NounPlur, npiFUTN, "N")
	futNonce = addToGram(VerbPlur, futNonce, "Vrel")
	futNonce = addToGram(ADJ, futNonce, "adj")

	hoegeNonce = addToGram(NounPlur, npiHN, "N")
	hoegeNonce = addToGram(VerbPlur, hoegeNonce, "Vrel")
	hoegeNonce = addToGram(VerbInf, hoegeNonce, "V")

	pn, pnfl = createLists(pastNonce)
	npiPastNonce = list(zip(pn, pnfl))

	fn, fnfl = createLists(futNonce)
	npiFutNonce = list(zip(fn, fnfl))

	hn, hnfl = createLists(hoegeNonce)
	npiHNonce = list(zip(hn, hnfl))

	writeTSV(ar_npiPast, ar_npiFut, ar_npiHoege, npiPastNonce, npiFutNonce, npiHNonce, "npiacrossrel_animate", "PAST", "FUTURE", "HOEGE", "PASTN", "FUTUREN", "HOEGEN")

if __name__ == '__main__':
	main()