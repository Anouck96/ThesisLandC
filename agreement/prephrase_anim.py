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
	with open("prepPh_animate_data.tsv", "w") as out_file:
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
	# Agreement across a prepositional phrase singular noun (with faulty inflections)
	prepsg = """ 
	S -> NP VPsi
	S -> NP VPpl
	NP -> NPs PP
	NPs -> Det Nsi
	PP -> Adp Detpl Npl
	Det -> 'in'
	Nsi -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Adp -> 'neist' | 'efter' | 'foar' | 'tsjinoer'
	Detpl -> 'de'
	Npl -> 'pakes' | 'boargemasters' | 'direkteuren' | 'prinsessen' | 'foarsitters' | 'prinsen'
	VPsi -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VPpl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'binne lang' | 'binne koart' | 'binne âld' | 'binne jong'
	"""

	# Optional both nouns singular
	prepsg2 = """ 
	S -> NP VPsi
	S -> NP VPpl
	NP -> NPs PP
	NPs -> Det Nsi
	PP -> Adp Detpl Ns2
	Det -> 'in'
	Nsi -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Adp -> 'neist' | 'efter' | 'foar' | 'tsjinoer'
	Detpl -> 'de'
	Ns2 -> 'pake' | 'boargemaster' | 'direkteur' | 'prinses' | 'foarsitter' | 'prins'
	VPsi -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VPpl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'binne lang' | 'binne koart' | 'binne âld' | 'binne jong'
	"""

	#Nonce singular
	prepsgNonce = """ 
	S -> NP VPsi
	S -> NP VPpl
	NP -> NPs PP
	NPs -> Det Nsi
	PP -> Adp Detpl Npl
	Det -> 'in'
	Adp -> 'neist' | 'efter' | 'foar' | 'tsjinoer'
	Detpl -> 'de'
	VPsi -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VPpl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'binne lang' | 'binne koart' | 'binne âld' | 'binne jong'
	"""

	# Agreement across a prepositional phrase plural noun (with faulty inflections)
	preppl = """ 
	S -> NP VPpl
	S -> NP VPsi
	NP -> NPs PP
	NPs -> Detpl Np1
	PP -> Adp Det Ns
	Det -> 'de'
	Np1 -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	Adp -> 'neist' | 'efter' | 'foar' | 'tsjinoer'
	Detpl -> 'de'
	Ns -> 'pake' | 'boargemaster' | 'direkteur' | 'prinses' | 'foarsitter' | 'prins'
	VPsi -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VPpl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'binne lang' | 'binne koart' | 'binne âld' | 'binne jong'
	"""

	# Optional both nouns plural
	preppl2 = """
	S -> NP VPpl
	S -> NP VPsi
	NP -> NPs PP
	NPs -> Detpl Np1
	PP -> Adp Det Npl
	Det -> 'de'
	Np1 -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	Adp -> 'neist' | 'efter' | 'foar' | 'tsjinoer'
	Detpl -> 'de'
	Npl -> 'pakes' | 'boargemasters' | 'direkteuren' | 'prinsessen' | 'foarsitters' | 'prinsen'
	VPsi -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VPpl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'binne lang' | 'binne koart' | 'binne âld' | 'binne jong'
	"""

	# Nonce plural
	prepplNonce = """ 
	S -> NP VPpl
	S -> NP VPsi
	NP -> NPs PP
	NPs -> Detpl Np1
	PP -> Adp Det Ns
	Det -> 'de'
	Adp -> 'neist' | 'efter' | 'foar' | 'tsjinoer'
	Detpl -> 'de'
	VPsi -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	VPpl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'binne lang' | 'binne koart' | 'binne âld' | 'binne jong'
	"""

	prepsg, prepsgfl = createLists(prepsg)
	prep_sing = list(zip(prepsg, prepsgfl))

	preppl, prepplfl = createLists(preppl)
	prep_plur = list(zip(preppl, prepplfl))

	prepsg2, prepsgfl2 = createLists(prepsg2)
	prep_sing2 = list(zip(prepsg2, prepsgfl2))

	preppl2, prepplfl2 = createLists(preppl2)
	prep_plur2 = list(zip(preppl2, prepplfl2))
	
	# Get random words
	NounSing = get_words("newRandomWords/prepostionalp/prepP1SingularNouns2804.csv")
	NounPlur = get_words("newRandomWords/prepostionalp/prepP1PluralNouns2804.csv")
	NounSing2 = get_words("newRandomWords/prepostionalp/prepP2SingularNouns2804.csv")
	NounPlur2 = get_words("newRandomWords/prepostionalp/prepP2PluralNouns2804.csv")

	noncesing = addToGram(NounSing, prepsgNonce, "Nsi")
	noncesing = addToGram(NounPlur2, noncesing, "Npl")
	noncesing, noncesingfl = createLists(noncesing)
	prepP_noncesing = list(zip(noncesing, noncesingfl))

	nonceplu = addToGram(NounPlur, prepplNonce, "Np1")
	nonceplu = addToGram(NounSing2, nonceplu, "Ns")
	nonceplu, nonceplufl = createLists(nonceplu)
	prepP_nonceplu = list(zip(nonceplu, nonceplufl))

	writeTSV(prep_sing, prep_plur, prepP_noncesing, prepP_nonceplu, prep_sing2, prep_plur2, "prepPhrase_anim", "prepPh_sing", "prepPh_plur", "prepPh_nonceSing", "prepPh_noncePlur", "prepPh_sing2", "prepPh_plur2")
if __name__ == '__main__':
	main()








	