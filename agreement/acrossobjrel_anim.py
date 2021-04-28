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
	with open("acrossobjrel_animate_data.tsv", "w") as out_file:
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

	# Across object relative clause (singular noun + faulty inflection)
	across_obj_relsg = """
	S -> NP VP VP2
	S -> NP VP VP2pl
	NP -> NP2 RelClause
	NP2 -> Det Nsi
	RelClause -> sconj VPrel
	VPrel -> Detpl Npl
	Det -> 'in'
	Detpl -> 'de'
	sconj -> "dy't"
	Nsi -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	VP -> 'fan hâlde' | 'bewûnderje' | 'haatsje'
	Npl -> 'pakes' | 'boargemasters' | 'direkteuren' | 'prinsessen' | 'foarsitters' | 'prinsen'
	VP2 -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VP2pl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	# Singular nonce
	across_obj_relsgNonce = """
	S -> NP VP VP2
	S -> NP VP VP2pl
	NP -> NP2 RelClause
	NP2 -> Det Nsi
	RelClause -> sconj VPrel
	VPrel -> Detpl Npl
	Det -> 'in'
	Detpl -> 'de'
	sconj -> "dy't"
	VP2 -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VP2pl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""
	# Optional all singulars
	across_obj_relsg2 = """
	S -> NP VP VP2
	S -> NP VP VP2pl
	NP -> NP2 RelClause
	NP2 -> Det Nsi
	RelClause -> sconj VPrel
	VPrel -> Det Nsg
	Det -> 'in'
	Detpl -> 'de'
	sconj -> "dy't"
	Nsi -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	VP -> 'fan hâldt' | 'bewûnderet' | 'hatet'
	Nsg -> 'pake' | 'boargemaster' | 'direkteur' | 'prinses' | 'foarsitter' | 'prins'
	VP2 -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VP2pl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	# Across object relative clause (plural noun + faulty inflection)
	across_obj_relpl = """
	S -> NP VP VP2pl
	S -> NP VP VP2
	NP -> NP2 RelClause
	NP2 -> Detpl Np
	RelClause -> sconj VPrel
	VPrel -> Det Nsg
	Det -> 'in'
	Detpl -> 'de'
	sconj -> "dy't"
	Np -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	VP -> 'fan hâldt' | 'bewûnderet' | 'hatet'
	Nsg -> 'pake' | 'boargemaster' | 'direkteur' | 'prinses' | 'foarsitter' | 'prins'
	VP2 -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VP2pl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	# Plural nonce
	across_obj_relplNonce = """
	S -> NP VP VP2pl
	S -> NP VP VP2
	NP -> NP2 RelClause
	NP2 -> Detpl Np
	RelClause -> sconj VPrel
	VPrel -> Det Nsg
	Det -> 'in'
	Detpl -> 'de'
	sconj -> "dy't"
	VP2 -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VP2pl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	# Optional all plurals
	across_obj_relpl2 = """
	S -> NP VP VP2pl
	S -> NP VP VP2
	NP -> NP2 RelClause
	NP2 -> Detpl Np
	RelClause -> sconj VPrel
	VPrel -> Detpl Np2
	Det -> 'in'
	Detpl -> 'de'
	sconj -> "dy't"
	Np -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	VP -> 'fan hâlde' | 'bewûnderje' | 'haatsje'
	Np2 -> 'pakes' | 'boargemasters' | 'direkteuren' | 'prinsessen' | 'foarsitters' | 'prinsen'
	VP2 -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VP2pl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	sing, singfl = createLists(across_obj_relsg)
	objrel_sing = list(zip(sing, singfl))

	plur, plurfl = createLists(across_obj_relpl)
	objrel_plur = list(zip(plur, plurfl))

	sing2, singfl2 = createLists(across_obj_relsg2)
	objrel_sing2 = list(zip(sing2, singfl2))

	plur2, plurfl2 = createLists(across_obj_relpl2)
	objrel_plur2 = list(zip(plur2, plurfl2))

# Get random words
	NounSing = get_words("newRandomWords/objrelclause/objrelSingularNouns2804.csv")
	NounPlur = get_words("newRandomWords/objrelclause/objrelPluralNouns2804.csv")
	NounSing2 = get_words("newRandomWords/objrelclause/objrel2SingularNouns2804.csv")
	NounPlur2 = get_words("newRandomWords/objrelclause/objrel2PluralNouns2804.csv")
	VerbSing = get_words("newRandomWords/objrelclause/objrelSingularVerbs2804.csv")
	VerbPlural = get_words("newRandomWords/objrelclause/objrelPluralVerbs2804.csv")

# Add to grammar and create minimal pairs
	noncesing = addToGram(NounSing, across_obj_relsgNonce, "Nsi")
	noncesing = addToGram(VerbPlural, noncesing, "VP")
	noncesing = addToGram(NounPlur2, noncesing, "Npl")
	nonces, noncesingfl = createLists(noncesing)
	acrosssubj_noncesing = list(zip(nonces, noncesingfl))

	nonceplur = addToGram(NounPlur, across_obj_relplNonce, "Np")
	nonceplur = addToGram(VerbSing, nonceplur, "VP")
	nonceplur = addToGram(NounSing2, nonceplur, "Nsg")
	noncep, nonceplurfl = createLists(nonceplur)
	acrosssubj_nonceplur = list(zip(noncep, nonceplurfl))



	writeTSV(objrel_sing, objrel_plur, acrosssubj_noncesing, acrosssubj_nonceplur, objrel_sing2, objrel_plur2, "across_objrel_anim", "acrossob_sg", "acrossob_pl", "acrossob_sgN", "acrossob_plN", "acrossob_sg2", "acrossob_pl2")


if __name__ == '__main__':
	main()