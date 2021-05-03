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
	with open("withinobj_inanimate_data.tsv", "w") as out_file:
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


	# within object relative clause (singular noun + faulty inflection)
	objInRel = """ 
	S -> NP Vrel VP
	S -> NP Vrels VP
	NP -> Nsi NPcomp
	NPcomp -> adp Detpl Npl
	Vrel -> 'hawwe'
	Vrels -> 'hat'
	VP -> 'is goed' | 'is min' | 'is nij' | 'is populêr'
	Nsi -> 'it hûs' | 'de auto' | 'it boek' | 'de tafel' | 'it ding'
	Npl -> 'pakes' | 'boargemasters' | 'direkteuren' | 'prinsessen' | 'foarsitters' | 'prinsen'
	adp -> 'dat'
	Detpl -> 'de'
	"""

	# Nonce singular
	objInRelNonce = """ 
	S -> NP Vrel VP
	S -> NP Vrels VP
	NP -> Det Nsi NPcomp
	NPcomp -> adp Detpl Npl
	Vrel -> 'hawwe'
	Vrels -> 'hat'
	adp -> 'dat'
	Detpl -> 'de'
	Det -> 'in'
	"""

	# Optional both singular
	objInRel2 = """ 
	S -> NP Vrels VP
	S -> NP Vrel VP
	NP -> Nsi NPcomp
	NPcomp -> adp Det N
	Vrel -> 'hawwe'
	Vrels -> 'hat'
	VP -> 'is goed' | 'is min' | 'is nij' | 'is populêr'
	Nsi -> 'it hûs' | 'de auto' | 'it boek' | 'de tafel' | 'it ding'
	N -> 'pake' | 'boargemaster' | 'direkteur' | 'prinses' | 'foarsitter' | 'prins'
	adp -> 'dat'
	Detpl -> 'de'
	Det -> 'in'
	"""

	# within object relative clause (plural noun + faulty inflection)
	objInRelpl = """ 
	S -> NP Vrelp VP
	S -> NP Vrel VP
	NP -> Detpl Npl NPcomp
	NPcomp -> adp Det N
	Vrel -> 'hawwe'
	Vrelp -> 'hat'
	VP -> 'benne goed' | 'benne min' | 'benne nij' | 'benne populêr'
	Npl -> 'huzen' | "auto's" | 'boeken' | 'tafels' | 'dingen'
	N -> 'pake' | 'boargemaster' | 'direkteur' | 'prinses' | 'foarsitter' | 'prins'
	adp -> "dy't"
	Detpl -> 'de'
	Det -> 'in'
	"""

	# Nonce plural
	objInRelplNonce = """ 
	S -> NP Vrelp VP
	S -> NP Vrel VP
	NP -> Detpl Npl NPcomp
	NPcomp -> adp Det N
	Vrel -> 'hawwe'
	Vrelp -> 'hat'
	adp -> "dy't"
	Detpl -> 'de'
	Det -> 'in'
	"""

	# Optional both plural
	objInRelpl2 = """ 
	S -> NP Vrel VP
	S -> NP Vrels VP
	NP -> Detpl Npl NPcomp
	NPcomp -> adp Detpl N
	Vrel -> 'hawwe'
	Vrels -> 'hat'
	VP -> 'benne goed' | 'benne min' | 'benne nij' | 'benne populêr'
	Npl -> 'huzen' | "auto's" | 'boeken' | 'tafels' | 'dingen'
	N -> 'pakes' | 'boargemasters' | 'direkteuren' | 'prinsessen' | 'foarsitters' | 'prinsen'
	adp -> "dy't"
	Detpl -> 'de'
	Det -> 'in'
	"""

	objinrel_sing, objinrel_singfl = createLists(objInRel)
	objinrel_sg = list(zip(objinrel_sing, objinrel_singfl))
	
	objinrel_plur, objinrel_plurfl = createLists(objInRelpl)
	objinrel_pl = list(zip(objinrel_plur, objinrel_plurfl))

	objinrel_sing2, objinrel_singfl2 = createLists(objInRel2)
	objinrel_sg2 = list(zip(objinrel_sing2, objinrel_singfl2))

	objinrel_plur2, objinrel_plurfl2 = createLists(objInRelpl2)
	objinrel_pl2 = list(zip(objinrel_plur2, objinrel_plurfl2))

	# Get random words
	NounSing = get_words("newRandomWords/withinobjrel/wobjrelSingularNouns3004.csv")
	NounPlur = get_words("newRandomWords/withinobjrel/wobjrelPluralNouns3004.csv")
	NounSing2 = get_words("newRandomWords/withinobjrel/wobjrelSingular2Nouns3004.csv")
	NounPlur2 = get_words("newRandomWords/withinobjrel/wobjrelPlural2Nouns3004.csv")
	VerbSing = get_words("newRandomWords/withinobjrel/wobjrelSingularVerbs3004.csv")
	VerbPlural = get_words("newRandomWords/withinobjrel/wobjrelPluralVerbs3004.csv")


# Add to grammar and create minimal pairs
	noncesing = addToGram(NounSing, objInRelNonce , "Nsi")
	noncesing = addToGram(VerbSing, noncesing, "VP")
	noncesing = addToGram(NounPlur2, noncesing, "Npl")
	nonces, noncesingfl = createLists(noncesing)
	wobjrel_noncesing = list(zip(nonces, noncesingfl))
	nonceplur = addToGram(VerbPlural, objInRelplNonce, "VP")
	nonceplur = addToGram(NounPlur, nonceplur, "Npl")
	nonceplur = addToGram(NounSing2, nonceplur, "N")
	noncep, noncepfl = createLists(nonceplur)
	wobjrel_nonceplur = list(zip(noncep, noncepfl))

	# names switched here (so sg is named pl except for sg2 and pl2)
	writeTSV(objinrel_sg, objinrel_pl, wobjrel_noncesing, wobjrel_nonceplur, objinrel_sg2, objinrel_pl2, "withinobjrel_inanim", "wobj_pl", "wojb_sg", "wobj_plNonce", "wobj_sgNonce", "wobj_sg2", "wobj_pl2")



if __name__ == '__main__':
	main()