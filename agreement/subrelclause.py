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
	with open("subrelclause_data.tsv", "w") as out_file:
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
	# Across subject relative clause (singular noun + faulty inflection)
	sub_relsg = """
	S -> NP VP2
	S -> NP VP2pl
	NP -> NP2 RelClause
	NP2 -> Det Nsi
	RelClause -> sconj VPrel
	VPrel -> Vrel Detpl Npl
	Det -> 'in'
	Detpl -> 'de'
	sconj -> "dy't"
	Nsi -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Vrel -> 'hâldt fan' | 'bewûnderet'
	Npl -> 'pakes' | 'boargemasters' | 'direkteuren' | 'prinsessen' | 'foarsitters' | 'prinsen'
	VP2 -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VP2pl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	# Nonce singular noun
	sub_relsgNonce = """
	S -> NP VP2
	S -> NP VP2pl
	NP -> NP2 RelClause
	NP2 -> Det Nsi
	RelClause -> sconj VPrel
	VPrel -> Vrel Detpl Npl
	Det -> 'in'
	Detpl -> 'de'
	sconj -> "dy't"
	VP2 -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VP2pl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	# Optional singular-singular
	sub_relsg2 = """
	S -> NP VP2
	S -> NP VP2pl
	NP -> NP2 RelClause
	NP2 -> Det Nsi
	RelClause -> sconj VPrel
	VPrel -> Vrel Det Npl
	Det -> 'in'
	Detpl -> 'de'
	sconj -> "dy't"
	Nsi -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Vrel -> 'hâldt fan' | 'bewûnderet'
	Npl -> 'pake' | 'boargemaster' | 'direkteur' | 'prinses' | 'foarsitter' | 'prins'
	VP2 -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VP2pl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	# Across subject relative clause (plural noun + faulty inflection)
	sub_relpl = """
	S -> NP VP2pl
	S -> NP VP2
	NP -> NP2 RelClause
	NP2 -> Detpl Nsi
	RelClause -> sconj VPrel
	VPrel -> Vrel Det Nsg
	Det -> 'in'
	Detpl -> 'de'
	sconj -> "dy't"
	Nsi -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	Vrel -> 'hâlde fan' | 'bewûnderje'
	Nsg -> 'pake' | 'boargemaster' | 'direkteur' | 'prinses' | 'foarsitter' | 'prins'
	VP2 -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VP2pl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	# Nonce plural noun
	sub_relplNonce = """
	S -> NP VP2pl
	S -> NP VP2
	NP -> NP2 RelClause
	NP2 -> Detpl Nplur
	RelClause -> sconj VPrel
	VPrel -> Vrel Det Nsg
	Det -> 'in'
	Detpl -> 'de'
	sconj -> "dy't"
	VP2 -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VP2pl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	# Optional plural-plural
	sub_relpl2 = """
	S -> NP VP2pl
	S -> NP VP2
	NP -> NP2 RelClause
	NP2 -> Detpl Nsi
	RelClause -> sconj VPrel
	VPrel -> Vrel Detpl Np
	Det -> 'in'
	Detpl -> 'de'
	sconj -> "dy't"
	Nsi -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	Vrel -> 'hâlde fan' | 'bewûnderje'
	Np -> 'pakes' | 'boargemasters' | 'direkteuren' | 'prinsessen' | 'foarsitters' | 'prinsen'
	VP2 -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VP2pl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	subsg, subsgfl = createLists(sub_relsg)
	subrel_sing = list(zip(subsg, subsgfl))

	subpl, subplfl = createLists(sub_relpl)
	subrel_plur = list(zip(subpl, subplfl))

	subsg2, subsgfl2 = createLists(sub_relsg2)
	subrel_sing2 = list(zip(subsg2, subsgfl2))

	subpl2, subsgfl2 = createLists(sub_relpl2)
	subrel_plur2 = list(zip(subpl2, subsgfl2))

# Get random words
	NounSing = get_words("newRandomWords/subrelclause/subrelSingularNouns2804.csv")
	NounPlur = get_words("newRandomWords/subrelclause/subrelPluralNouns2804.csv")
	NounSing2 = get_words("newRandomWords/subrelclause/subrel2SingularNouns2804.csv")
	NounPlur2 = get_words("newRandomWords/subrelclause/subrel2PluralNouns2804.csv")
	VerbSing = get_words("newRandomWords/subrelclause/subrelSingularVerbs2804.csv")
	VerbPlural = get_words("newRandomWords/subrelclause/subrelPluralVerbs2804.csv")

# Add to grammar and create minimal pairs
	noncesing = addToGram(NounSing, sub_relsgNonce, "Nsi")
	noncesing = addToGram(NounPlur2, noncesing, "Npl")
	noncesing = addToGram(VerbSing, noncesing, "Vrel")
	nonces, noncesingfl = createLists(noncesing)
	prepP_noncesing = list(zip(nonces, noncesingfl))

	nonceplur = addToGram(NounPlur, sub_relplNonce, "Nplur")
	nonceplur = addToGram(NounSing2, nonceplur, "Nsg")
	nonceplur = addToGram(VerbPlural, nonceplur, "Vrel")
	noncep, noncepfl = createLists(nonceplur)
	prepP_nonceplur = list(zip(noncep, noncepfl))

	writeTSV(subrel_sing, subrel_plur, prepP_noncesing, prepP_nonceplur, subrel_sing2, subrel_plur2, "across_sub_rel", "subrel_sing", "subrel_plur", "subrelnonce_sing", "subrelnonce_plur", "subrel_sing2", "subrel_plur2")

if __name__ == '__main__':
	main()
























