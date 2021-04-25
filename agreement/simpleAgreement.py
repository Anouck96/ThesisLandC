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

	return PairsList

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

def writeTSV(SimpAgrSingular, SimpAgrPlural, simpagrSingNonce, simpagrnonceplural, Nsimp_agrmt, Nsa, Npa, Nsn, Npn):
	with open("simpagr_data.tsv", "w") as out_file:
		tsv_output = csv.writer(out_file, delimiter='\t')

		# Write minimal pairs singular
		for it in SimpAgrSingular:
			start = [Nsimp_agrmt, Nsa]
			start.extend(it)
			tsv_output.writerow(start)
	
		# Write minimal pairs plural
		for i in SimpAgrPlural:
			stplu = [Nsimp_agrmt, Npa]
			stplu.extend(i)
			tsv_output.writerow(stplu)

		# Write minimal pairs singular nonce
		for p in simpagrSingNonce:
			sinnonce = [Nsimp_agrmt, Nsn]
			sinnonce.extend(p)
			tsv_output.writerow(sinnonce)

		# Write minimal pairs plural nonce
		for pp in simpagrnonceplural:
			plunonce = [Nsimp_agrmt, Npn]
			plunonce.extend(pp)
			tsv_output.writerow(plunonce)

def main():

# Singular Noun simple agreement
	simpAgrSing = """
	S -> NP VP
	VP -> V
	NP -> Det N
	NP -> Propn
	Det -> 'in'
	N -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Propn -> 'ypeij' | 'anneke' | 'durk' | 'nikolaas'
	V -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	"""

# For creation of nonce
	simpSingNonce = """
	S -> NP VP
	VP -> V
	NP -> Det N
	NP -> Propn
	Det -> 'in'
	"""

# Singular Noun with faulty plural verb
	simpAgrSingFault = """ 
	S -> NP VP
	VP -> V
	NP -> Det N
	NP -> Propn
	Det -> 'in'
	N -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Propn -> 'ypeij' | 'anneke' | 'durk' | 'nikolaas'
	V -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""


# Plural Noun simple agreement
	simpAgrPlCor = """ 
	S -> NP VP
	VP -> V
	NP -> Det N
	NP -> Propn
	Det -> 'de'
	N -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	V -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

# For nonce sentences plural noun correct
	noncepluc = """ 
	S -> NP VP
	VP -> V
	NP -> Det N
	NP -> Propn
	Det -> 'de'
	"""

# Plural Noun with faulty singular verb
	simpAgrPlFault = """
	S -> NP VP
	VP -> V
	NP -> Det N
	NP -> Propn
	Det -> 'de'
	N -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	V -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	"""


	MinPairsSingCor = createLists(simpAgrSing)
	MinPairsSingFa = createLists(simpAgrSingFault)
	MinPairsPlurCor = createLists(simpAgrPlCor)
	MinPairsPlurFa = createLists(simpAgrPlFault)


	# Get random words from csv files
	NOUNsing = get_words("newRandomWords/simpleAgreement/SimpleAgreementSingularNounsbijV.csv")
	NOUNpl = get_words("newRandomWords/simpleAgreement/SimpleAgreementPluralNounsbijV.csv")
	VERBsing = get_words("newRandomWords/simpleAgreement/SimpleAgreementSingularVerbs.csv")
	VERBpl = get_words("newRandomWords/simpleAgreement/SimpleAgreementPluralVerbs.csv")

	noncesing = addToGram(NOUNsing, simpSingNonce, "N")
	noncesing = noncesing + "\n" + "V -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'"
	minnoncesingcor = createLists(noncesing)

	noncesingFl = addToGram(NOUNsing, simpSingNonce, "N")
	noncesingFl = noncesingFl + "\n" + "V -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'"
	minnoncesingfaul = createLists(noncesingFl)

	nonceplucor = addToGram(NOUNpl, noncepluc, "N")
	nonceplucor = nonceplucor + "\n" + "V -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'"
	mpnonceplurcor = createLists(nonceplucor)


	nonceplufl = addToGram(NOUNpl, noncepluc, "N")
	nocneplufl = nonceplufl + "\n" + "V -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'"
	mpnonceplurfaul = createLists(nocneplufl)

	#Create minimal pairs
	SimpAgrSingular = list(zip(MinPairsSingCor, MinPairsSingFa))
	SimpAgrPlural = list(zip(MinPairsPlurCor, MinPairsPlurFa))
	simpagrSingNonce = list(zip(minnoncesingcor, minnoncesingfaul))
	simpagrnonceplural = list(zip(mpnonceplurcor, mpnonceplurfaul))

	# Write to tsv file

	writeTSV(SimpAgrSingular, SimpAgrPlural, simpagrSingNonce, simpagrnonceplural, "simp_agrmt", "sing_agr", "plur_agr", "sing_nonce", "plural_nonce")

if __name__ == '__main__':
	main()