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

def writeTSV(sing, plu, sing2, plu2, mainName, s, p, ss, pp):
	with open("acrossobjrel_inanimate_data.tsv", "w") as out_file:
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
	NP2 -> Nsi
	RelClause -> sconj VPrel
	VPrel -> Detpl Npl
	Det -> 'in'
	Detpl -> 'de'
	sconj -> "der't"
	Nsi -> 'it hûs' | 'de auto' | 'it boek' | 'de tafel' | 'it ding'
	VP -> 'fan hâlde' | 'bewûnderje' | 'haatsje'
	Npl -> 'pakes' | 'boargemasters' | 'direkteuren' | 'prinsessen' | 'foarsitters' | 'prinsen'
	VP2 -> 'is goed' | 'is min' | 'is nij' | 'is populêr'
	VP2pl -> 'binne goed' | 'binne min' | 'binne nij' | 'binne populêr'
	"""

	# Optional all singulars
	across_obj_relsg2 = """
	S -> NP VP VP2
	S -> NP VP VP2pl
	NP -> NP2 RelClause
	NP2 -> Nsi
	RelClause -> sconj VPrel
	VPrel -> Det Nsg
	Det -> 'in'
	Detpl -> 'de'
	sconj -> "der't"
	Nsi -> 'it hûs' | 'de auto' | 'it boek' | 'de tafel' | 'it ding'
	VP -> 'fan hâldt' | 'bewûnderet' | 'hatet'
	Nsg -> 'pake' | 'boargemaster' | 'direkteur' | 'prinses' | 'foarsitter' | 'prins'
	VP2 -> 'is goed' | 'is min' | 'is nij' | 'is populêr'
	VP2pl -> 'binne goed' | 'binne min' | 'binne nij' | 'binne populêr'
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
	sconj -> "der't"
	Np -> 'huzen' | "auto's" | 'boeken' | 'tafels' | 'dingen'
	VP -> 'fan hâldt' | 'bewûnderet' | 'hatet'
	Nsg -> 'pake' | 'boargemaster' | 'direkteur' | 'prinses' | 'foarsitter' | 'prins'
	VP2 -> 'is goed' | 'is min' | 'is nij' | 'is populêr'
	VP2pl -> 'binne goed' | 'binne min' | 'binne nij' | 'binne populêr'
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
	sconj -> "der't"
	Np -> 'huzen' | "auto's" | 'boeken' | 'tafels' | 'dingen'
	VP -> 'fan hâlde' | 'bewûnderje' | 'haatsje'
	Np2 -> 'pakes' | 'boargemasters' | 'direkteuren' | 'prinsessen' | 'foarsitters' | 'prinsen'
	VP2 -> 'is goed' | 'is min' | 'is nij' | 'is populêr'
	VP2pl -> 'binne goed' | 'binne min' | 'binne nij' | 'binne populêr'
	"""

	sing, singfl = createLists(across_obj_relsg)
	objrel_sing = list(zip(sing, singfl))

	plur, plurfl = createLists(across_obj_relpl)
	objrel_plur = list(zip(plur, plurfl))

	sing2, singfl2 = createLists(across_obj_relsg2)
	objrel_sing2 = list(zip(sing2, singfl2))

	plur2, plurfl2 = createLists(across_obj_relpl2)
	objrel_plur2 = list(zip(plur2, plurfl2))


	writeTSV(objrel_sing, objrel_plur, objrel_sing2, objrel_plur2, "across_objrel_inanim", "acrossob_sg", "acrossob_pl", "acrossob_sg2", "acrossob_pl2")
if __name__ == '__main__':
	main()