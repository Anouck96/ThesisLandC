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

def writeTSV(SimpAgrSingular, SimpAgrPlural, simpagrSingNonce, simpagrnonceplural, sentcomsingSwitch, sentcomplurSwitch, Nsimp_agrmt, Nsa, Npa, Nsn, Npn, scsS, scpS):
	with open("sentComp_data.tsv", "w") as out_file:
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

		# Write minimal pairs singular switched
		for s in sentcomsingSwitch:
			st = [Nsimp_agrmt, scsS]
			st.extend(s)
			tsv_output.writerow(st)

		# Write minimal pairs singular switched
		for e in sentcomplurSwitch:
			swp = [Nsimp_agrmt, scpS]
			swp.extend(e)
			tsv_output.writerow(swp)

def main():	
	# Agreement in sentential complement sing NP (with faulty inflection)
	sent_compCor = """
	S -> NP VP Cp
	S -> NP VP Cpfl
	NP -> Detpl Npl
	Cp -> sconj Vpcomp
	Cpfl -> sconj Vpcompfl
	Vpcomp -> Det Nsing Vsing
	Vpcompfl -> Det Nsing Vplur
	Det -> 'in'
	Detpl -> 'de'
	Npl -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	VP -> 'tochten' | 'wisten'
	Nsing -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Vsing -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'lang is' | 'koart is' | 'âld is' | 'jong is'
	Vplur -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'lang binne' | 'koart binne' | 'âld binne' | 'jong binne'
	sconj -> 'dat'
	"""

	# Optional (singular first noun and singular inflection)
	sent_compCorSwitch = """
	S -> NP VP Cp
	S -> NP VP Cpfl
	NP -> Det Nsing
	Cp -> sconj Vpcomp
	Cpfl -> sconj Vpcompfl
	Vpcomp -> Det Nsing Vsing
	Vpcompfl -> Det Nsing Vplur
	Det -> 'in'
	Detpl -> 'de'
	Npl -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	VP -> 'tocht' | 'wist'
	Nsing -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Vsing -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'lang is' | 'koart is' | 'âld is' | 'jong is'
	Vplur -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'lang binne' | 'koart binne' | 'âld binne' | 'jong binne'
	sconj -> 'dat'
	"""

	# Nonce version
	sent_compCorNonce = """
	S -> NP VP Cp
	S -> NP VP Cpfl
	NP -> Detpl Npl
	Cp -> sconj Vpcomp
	Cpfl -> sconj Vpcompfl
	Vpcomp -> Det Nsing Vsing
	Vpcompfl -> Det Nsing Vplur
	Det -> 'in'
	Detpl -> 'de'
	sconj -> 'dat'
	Vsing -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'lang is' | 'koart is' | 'âld is' | 'jong is'
	Vplur -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'lang binne' | 'koart binne' | 'âld binne' | 'jong binne'
	"""
	# Agreement in sentential complement plural NP (with faulty inflection)
	sent_compplCor = """
	S -> NP VP Cp
	S -> NP VP Cpfl
	NP -> Det Nsing
	Cp -> sconj Vpcomp
	Cpfl -> sconj Vpcompfl
	Vpcomp -> Detpl Npl Vplur
	Vpcompfl -> Detpl Npl Vsing
	Det -> 'in'
	Detpl -> 'de'
	Npl -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	VP -> 'tocht' | 'wist'
	Nsing -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Vplur -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'lang binne' | 'koart binne' | 'âld binne' | 'jong binne'
	sconj -> 'dat'
	Vsing -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'lang is' | 'koart is' | 'âld is' | 'jong is'
	"""

	# Optional both nouns plural
	sent_compplswitch = """
	S -> NP VP Cp
	S -> NP VP Cpfl
	NP -> Detpl Npl
	Cp -> sconj Vpcomp
	Cpfl -> sconj Vpcompfl
	Vpcomp -> Detpl Npl Vplur
	Vpcompfl -> Detpl Npl Vsing
	Det -> 'in'
	Detpl -> 'de'
	Npl -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	VP -> 'tochten' | 'wisten'
	Nsing -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Vplur -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'lang binne' | 'koart binne' | 'âld binne' | 'jong binne'
	sconj -> 'dat'
	Vsing -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'lang is' | 'koart is' | 'âld is' | 'jong is'
	"""


	# Nonce version
	sent_compplNonce = """
	S -> NP VP Cp
	S -> NP VP Cpfl
	NP -> Det Nsing
	Cp -> sconj Vpcomp
	Cpfl -> sconj Vpcompfl
	Vpcomp -> Detpl Npl Vplur
	Vpcompfl -> Detpl Npl Vsing
	Det -> 'in'
	Detpl -> 'de'
	sconj -> 'dat'
	Vsing -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'lang is' | 'koart is' | 'âld is' | 'jong is'
	Vplur -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'lang binne' | 'koart binne' | 'âld binne' | 'jong binne'
	"""

	corsing, flsing = createLists(sent_compCor)
	corplur, flplur = createLists(sent_compplCor)

	corsingSwitch, flsingSwitch = createLists(sent_compCorSwitch)
	corplurSwitch, flplurSwitch = createLists(sent_compplswitch)
	 # Create minimal pairs
	sentComp_Sing = list(zip(corsing, flsing))
	sentComp_Plur = list(zip(corplur, flplur))

	sentCompSingSwitch = list(zip(corsingSwitch, flsingSwitch))
	sentCompPlurSwitch = list(zip(corplurSwitch, flplurSwitch))

	# Get random words
	NounSing = get_words("newRandomWords/sentComp/SentCompSingularNouns.csv")
	NounPlur = get_words("newRandomWords/sentComp/SentCompPluralNouns.csv")
	Verbs2Sing = get_words("newRandomWords/sentComp/SentComp2SingularVerbs.csv")
	Verbs2Plur = get_words("newRandomWords/sentComp/SentComp2PluralVerbs.csv")

	 # Create nonce sentence singular
	noncesing = addToGram(NounSing, sent_compCorNonce, "Nsing")
	noncesing = addToGram(Verbs2Plur, noncesing, "VP")
	noncesing = addToGram(NounPlur, noncesing, "Npl")
	noncesing, noncesingfl = createLists(noncesing)
	sentComp_noncesing = list(zip(noncesing, noncesingfl))


	 #Create nonce sentences plural
	nonceplur = addToGram(NounPlur, sent_compplNonce, "Npl")
	nonceplur = addToGram(Verbs2Sing, nonceplur, "VP")
	nonceplur = addToGram(NounSing,nonceplur, "Nsing")
	nonceplur, nonceplurfl = createLists(nonceplur)
	sentComp_nonceplur = list(zip(nonceplur, nonceplurfl))

	writeTSV(sentComp_Sing, sentComp_Plur, sentComp_noncesing, sentComp_nonceplur, sentCompSingSwitch, sentCompPlurSwitch, "sent_comp", "sent_compSing", "sent_compPlur", "sent_compNonceSing", "sent_compNoncePlur", "sent_compSingSwitch", "sent_compPlurSwitch")	

if __name__ == '__main__':
	main()