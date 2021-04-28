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
	print(subrel_plur2)
if __name__ == '__main__':
	main()