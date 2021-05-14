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
	with open("prepPh_inanimate_data.tsv", "w") as out_file:
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
	# Agreement across a prepositional phrase singular noun (with faulty inflections)
	prepsg = """ 
	S -> NP VPsi
	S -> NP VPpl
	NP -> NPs PP
	NPs -> Nsi
	PP -> Adp Detpl Npl
	Nsi -> 'it hûs' | 'de auto' | 'it boek' | 'de tafel' | 'it ding'
	Adp -> 'neist' | 'efter' | 'foar' | 'tichtby' | 'tsjinoer'
	Detpl -> 'de'
	Npl -> 'pakes' | 'boargemasters' | 'direkteuren' | 'prinsessen' | 'foarsitters' | 'prinsen'
	VPsi -> 'is goed' | 'is min' | 'is nij' | 'is populêr'
	VPpl -> 'binne goed' | 'binne min' | 'binne nij' | 'binne populêr'
	""" 

	# Optional both nouns singular
	prepsg2 = """ 
	S -> NP VPsi
	S -> NP VPpl
	NP -> NPs PP
	NPs -> Nsi
	PP -> Adp Detpl Ns2
	Nsi -> 'it hûs' | 'de auto' | 'it boek' | 'de tafel' | 'it ding'
	Adp -> 'neist' | 'efter' | 'foar' | 'tichtby' | 'tsjinoer'
	Detpl -> 'de'
	Ns2 -> 'pake' | 'boargemaster' | 'direkteur' | 'prinses' | 'foarsitter' | 'prins'
	VPsi -> 'is goed' | 'is min' | 'is nij' | 'is populêr'
	VPpl -> 'binne goed' | 'binne min' | 'binne nij' | 'binne populêr'
	"""

	# Agreement across a prepositional phrase plural noun (with faulty inflections)
	preppl = """ 
	S -> NP VPpl
	S -> NP VPsi
	NP -> NPs PP
	NPs -> Detpl Np1
	PP -> Adp Det Ns
	Det -> 'de'
	Np1 -> 'huzen' | "auto's" | 'boeken' | 'tafels' | 'dingen'
	Adp -> 'neist' | 'efter' | 'foar' | 'tichtby' | 'tsjinoer'
	Detpl -> 'de'
	Ns -> 'pake' | 'boargemaster' | 'direkteur' | 'prinses' | 'foarsitter' | 'prins'
	VPsi -> 'is goed' | 'is min' | 'is nij' | 'is populêr'
	VPpl -> 'binne goed' | 'binne min' | 'binne nij' | 'binne populêr'
	"""

	# Optional both nouns plural
	preppl2 = """
	S -> NP VPpl
	S -> NP VPsi
	NP -> NPs PP
	NPs -> Detpl Np1
	PP -> Adp Det Npl
	Det -> 'de'
	Np1 -> 'huzen' | "auto's" | 'boeken' | 'tafels' | 'dingen'
	Adp -> 'neist' | 'efter' | 'foar' | 'tichtby' | 'tsjinoer'
	Detpl -> 'de'
	Npl -> 'pakes' | 'boargemasters' | 'direkteuren' | 'prinsessen' | 'foarsitters' | 'prinsen'
	VPsi -> 'is goed' | 'is min' | 'is nij' | 'is populêr'
	VPpl -> 'binne goed' | 'binne min' | 'binne nij' | 'binne populêr'
	"""

	prepsg, prepsgfl = createLists(prepsg)
	prep_sing = list(zip(prepsg, prepsgfl))

	preppl, prepplfl = createLists(preppl)
	prep_plur = list(zip(preppl, prepplfl))

	prepsg2, prepsgfl2 = createLists(prepsg2)
	prep_sing2 = list(zip(prepsg2, prepsgfl2))

	preppl2, prepplfl2 = createLists(preppl2)
	prep_plur2 = list(zip(preppl2, prepplfl2))
	

	writeTSV(prep_sing, prep_plur, prep_sing2, prep_plur2, "prepPhrase_inanim", "prepPh_sing", "prepPh_plur", "prepPh_sing2", "prepPh_plur2")
if __name__ == '__main__':
	main()








	