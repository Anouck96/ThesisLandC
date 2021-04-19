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
	with open("sent_comp.tsv", "w") as out_file:
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
	# Agreement in sentential complement sing NP (with faulty inflection)
	sent_compCor = """
	S -> NP VP Cp PUNCT
	NP -> Detpl Npl
	Cp -> sconj Vpcomp
	Vpcomp -> Det Nsing Vsing
	Det -> 'in'
	Detpl -> 'de'
	Npl -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	VP -> 'seinen' | 'seagen' | 'tochten' | 'wisten'
	Nsing -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Vsing -> 'giet' | 'komt' | 'freget' | 'stiet' | 'rûn' | 'sit' | 'praat' 
	sconj -> 'dat'
	PUNCT -> '.'
	"""

	# Nonce version
	sent_compCorNonce = """
	S -> NP VP Cp PUNCT
	NP -> Detpl Npl
	Cp -> sconj Vpcomp
	Vpcomp -> Det Nsing V
	Det -> 'in'
	Detpl -> 'de'
	sconj -> 'dat'
	PUNCT -> '.'
	"""

	# Faulty version
	sent_compFault = """
	S -> NP VP Cp PUNCT
	NP -> Detpl Npl
	Cp -> sconj Vpcomp
	Vpcomp -> Det Nsing Vplur
	Det -> 'in'
	Detpl -> 'de'
	Npl -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	VP -> 'seinen' | 'seagen' | 'tochten' | 'wisten'
	Nsing -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Vplur -> 'geane' | 'komme' | 'freegje' | 'steane' | 'rinne' |'sitte' | 'prate'
	sconj -> 'dat'
	PUNCT -> '.'
	"""

	# Agreement in sentential complement plural NP
	sent_compplCor = """
	S -> NP VP Cp PUNCT
	NP -> Det Nsing
	Cp -> sconj Vpcomp
	Vpcomp -> Detpl Npl Vplur
	Det -> 'in'
	Detpl -> 'de'
	Npl -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	VP -> 'sei' | 'seach' | 'tocht' | 'wist'
	Nsing -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Vplur -> 'geane' | 'komme' | 'freegje' | 'steane' | 'rinne' |'sitte' | 'prate'
	sconj -> 'dat'
	PUNCT -> '.'
	"""

	# Agreement in sentential complement plural NP Faulty inflection
	sent_compplFault = """
	S -> NP VP Cp PUNCT
	NP -> Det Nsing
	Cp -> sconj Vpcomp
	Vpcomp -> Detpl Npl Vsing
	Det -> 'in'
	Detpl -> 'de'
	Npl -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	VP -> 'sei' | 'seach' | 'tocht' | 'wist'
	Nsing -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Vsing -> 'giet' | 'komt' | 'freget' | 'stiet' | 'rûn' | 'sit' | 'praat'
	sconj -> 'dat'
	PUNCT -> '.'
	"""

	# Nonce version
	sent_compplNonce = """
	S -> NP VP Cp PUNCT
	NP -> Det Nsing
	Cp -> sconj Vpcomp
	Vpcomp -> Detpl Npl V
	Det -> 'in'
	Detpl -> 'de'
	sconj -> 'dat'
	PUNCT -> '.'
	"""

	sent_compSingCorrect = createLists(sent_compCor)
	sent_compSingFaulty = createLists(sent_compFault)
	sent_compPluCor = createLists(sent_compplCor)
	sent_compPluFaulty = createLists(sent_compplFault)
	# Create minimal pairs
	sent_compSing = list(zip(sent_compSingCorrect, sent_compSingFaulty))
	sent_compPlur = list(zip(sent_compPluCor, sent_compPluFaulty))

	NounSing = get_words("newRandomWords/sentComp/SentCompSingularNouns.csv")
	NounPlur = get_words("newRandomWords/sentComp/SentCompPluralNouns.csv")
	VerbSing = get_words("newRandomWords/sentComp/SentCompSingularVerbs.csv")
	VerbPlur = get_words("newRandomWords/sentComp/SentCompPluralVerbs.csv")
	Verbs2Sing = get_words("newRandomWords/sentComp/SentComp2SingularVerbs.csv")
	Verbs2Plur = get_words("newRandomWords/sentComp/SentComp2PluralVerbs.csv")

	# Create nonce sentence singular
	noncesing = addToGram(NounSing, sent_compCorNonce, "Nsing")
	noncesing = addToGram(VerbSing, noncesing, "V")
	noncesing = addToGram(Verbs2Plur, noncesing, "VP")
	noncesing = addToGram(NounPlur, noncesing, "Npl")
	NonceSingCor = createLists(noncesing)

	# Create nonce sentences singular faulty inflection
	noncesingf = addToGram(NounSing, sent_compCorNonce, "Nsing")
	noncesingf = addToGram(VerbPlur, noncesingf, "V")
	noncesingf = addToGram(Verbs2Plur, noncesingf, "VP")
	noncesingf = addToGram(NounPlur, noncesingf, "Npl")
	NonceSingFl = createLists(noncesingf)

	#Create nonce sentences plural
	nonceplur = addToGram(NounPlur, sent_compplNonce, "Npl")
	nonceplur = addToGram(Verbs2Sing, nonceplur, "VP")
	nonceplur = addToGram(NounSing,nonceplur, "Nsing")
	nonceplur = addToGram(VerbPlur, nonceplur, "V")
	NoncePlurCor = createLists(nonceplur)

	# Create nonce sentences plural faulty inflection
	nonceplurf = addToGram(NounPlur, sent_compplNonce, "Npl")
	nonceplurf = addToGram(Verbs2Sing, nonceplurf, "VP")
	nonceplurf = addToGram(NounSing,nonceplurf, "Nsing")
	nonceplurf = addToGram(VerbSing, nonceplurf, "V")
	NoncePlurF = createLists(nonceplurf)

	#Create minimal pairs
	sent_compNonceSing = list(zip(NonceSingCor, NonceSingFl))
	sent_compNoncePlur = list(zip(NoncePlurCor, NoncePlurF))

	writeTSV(sent_compSing, sent_compPlur, sent_compNonceSing, sent_compNoncePlur, "sent_comp", "sent_compSing", "sent_compPlur", "sent_compNonceSing", "sent_compNoncePlur")	

if __name__ == '__main__':
	main()