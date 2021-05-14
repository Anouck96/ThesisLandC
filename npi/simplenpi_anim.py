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
	with open("simplenpi_animate_data.tsv", "w") as out_file:
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

	# simple NPI (PAST)
	npiPAST = """
	S -> NP1 aux VP
	S -> NP2 aux VP
	NP1 -> neg N
	NP2 -> det N
	aux -> 'binne'
	VP -> npi adj Vpartic
	neg -> 'gjin'
	det -> 'de'
	npi -> 'ea' 
	adj -> 'populêr' | 'ferneamd' | 'earste' | 'goed' | 'moai'
	Vpartic -> 'west'
	N -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	"""

	# simple NPI (FUTURE)
	npiFUT = """
	S -> NP1 aux VP
	S -> NP2 aux VP
	NP1 -> neg N
	NP2 -> det N
	aux -> 'sille'
	VP -> npi adj Vpartic
	neg -> 'gjin'
	det -> 'de'
	npi -> 'ea' 
	adj -> 'populêr' | 'ferneamd' | 'earste' | 'goed' | 'moai'
	Vpartic -> 'wêze'
	N -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	"""

	# simple NPI (PAST) NONCE
	npiPASTNONCE = """
	S -> NP1 aux VP
	S -> NP2 aux VP
	NP1 -> neg N
	NP2 -> det N
	aux -> 'binne'
	VP -> npi adj Vpartic
	neg -> 'gjin'
	det -> 'de'
	npi -> 'ea' 
	Vpartic -> 'west'
	"""
	# simple NPI (FUTURE) NONCE
	npiFUTN = """
	S -> NP1 aux VP
	S -> NP2 aux VP
	NP1 -> neg N
	NP2 -> det N
	aux -> 'sille'
	VP -> npi adj Vpartic
	neg -> 'gjin'
	det -> 'de'
	npi -> 'ea' 
	Vpartic -> 'wêze'
	"""

	# NPI with "hoege"
	npiH = """
	S -> NP aux npi VP
	S -> NP aux adj VP
	NP -> det N
	VP -> adp V
	det -> 'de'
	npi -> 'net'
	adj -> 'wol'
	N -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	aux -> 'hoege'
	adp -> 'te'
	V -> 'sizze' | 'wolle' | 'gean' |'stean'
	"""

	# NPI with "hoege" and nonce
	npiHN = """
	S -> NP aux npi VP
	S -> NP aux adj VP
	NP -> det N
	VP -> adp V
	det -> 'de'
	npi -> 'net'
	adj -> 'wol'
	aux -> 'hoege'
	adp -> 'te'
	"""


	past, pastfl = createLists(npiPAST)
	npiP = list(zip(past, pastfl))
	fut, futfl = createLists(npiFUT)
	npiF = list(zip(fut, futfl))
	hoege, hoegefl = createLists(npiH)
	npiHoege = list(zip(hoege, hoegefl))

	# Get random words
	NounPl = get_words("randomWords/simpleNPI/simpNPIPluralNouns3004.csv")
	VerbPl = get_words("randomWords/simpleNPI/simpNPIPluralVerbs3004.csv")
	ADJ = get_words("randomWords/simpleNPI/simpNPIADJ3004.csv")

	npiPNonce = addToGram(NounPl, npiPASTNONCE, "N")
	npiPNonce = addToGram(ADJ, npiPNonce, "adj")
	npiPNc, npiPNfl = createLists(npiPNonce)
	npiPastNon = list(zip(npiPNc, npiPNfl))

	npiFNonce = addToGram(NounPl, npiFUTN, "N")
	npiFNonce = addToGram(ADJ, npiFNonce, "adj")
	npiFNc, npiFNfl = createLists(npiFNonce)
	npiFutNon = list(zip(npiFNc, npiFNfl))

	hnpi = addToGram(NounPl, npiHN, "N")
	hnpi = addToGram(VerbPl, hnpi, "V")
	npiHc, npiHfl = createLists(hnpi)
	npiHNonce = list(zip(npiHc, npiHfl))

	writeTSV(npiP, npiF, npiHoege, npiPastNon, npiFutNon, npiHNonce, "SimpleNPI", "PAST", "FUTURE", "npiWHoege", "PAST_NONCE", "FUTURE_NONCE", "npiWHoege_NONCE")

if __name__ == '__main__':
	main()