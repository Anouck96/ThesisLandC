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

# Singular Noun simple agreement with faulty inflections
	simpAgrSing = """
	S -> NP VP
	S -> NP Vpl
	VP -> V
	NP -> Det N
	NP -> Propn
	Det -> 'in'
	N -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Propn -> 'ypeij' | 'anneke' | 'durk' | 'nikolaas'
	V -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	Vpl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

# Plural Noun simple agreement
	simpAgrPl = """ 
	S -> NP VP
	S -> NP Vsi
	VP -> V
	NP -> Det N
	NP -> Propn
	Det -> 'de'
	N -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	V -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	Vsi -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	"""

# For creation of nonce
	simpAgrNonce = """
	S -> NP VP
	S -> NP Vfl
	VP -> V
	NP -> Det N
	NP -> Propn
	"""

	SingCor, SingFl = createLists(simpAgrSing)
	PluCor, PluFl = createLists(simpAgrPl)

		# Get random words from csv files
	NOUNsing = get_words("newRandomWords/simpleAgreement/SingularNouns2704.csv")
	NOUNpl = get_words("newRandomWords/simpleAgreement/PluralNouns2704.csv")

	noncesing = addToGram(NOUNsing, simpAgrNonce, "N")
	noncesing = noncesing + "\n" + "V -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit'"
	noncesing = noncesing + "\n" + "Vfl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige'"
	noncesing = noncesing + "\n" + "Det -> 'in'"
	noncesingCor, noncesingFl = createLists(noncesing)

	nonceplucor = addToGram(NOUNpl, simpAgrNonce, "N")
	nonceplucor = nonceplucor + "\n" + "V -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige'"
	nonceplucor = nonceplucor + "\n" + "Det -> 'de'"
	nonceplucor = nonceplucor + "\n" + "Vfl -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit'"
	noncepluCor, noncepluFl = createLists(nonceplucor)


#Create minimal pairs
	SimpAgrSingular = list(zip(SingCor, SingFl))
	SimpAgrPlural = list(zip(PluCor, PluFl))
	NonceSimpAgrSing = list(zip(noncesingCor, noncesingFl))
	NonceSimpAgrPlu = list(zip(noncepluCor, noncepluFl))
# Write to tsv
	writeTSV(SimpAgrSingular, SimpAgrPlural, NonceSimpAgrSing, NonceSimpAgrPlu, "simp_agrmt", "sing_agr", "plur_agr", "sing_nonce", "plural_nonce")

if __name__ == '__main__':
	main()