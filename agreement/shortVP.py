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

def writeTSV(Sing, Plur, SingNonce, PlurNonce, mainName, S, P, SN, PN):
	with open("shortVP_data.tsv", "w") as out_file:
		tsv_output = csv.writer(out_file, delimiter='\t')

		# Write minimal pairs singular
		for it in Sing:
			start = [mainName, S]
			start.extend(it)
			tsv_output.writerow(start)
	
		# Write minimal pairs plural
		for i in Plur:
			stplu = [mainName, P]
			stplu.extend(i)
			tsv_output.writerow(stplu)

		# Write minimal pairs singular nonce
		for p in SingNonce:
			sinnonce = [mainName, SN]
			sinnonce.extend(p)
			tsv_output.writerow(sinnonce)

		# Write minimal pairs plural nonce
		for pp in PlurNonce:
			plunonce = [mainName, PN]
			plunonce.extend(pp)
			tsv_output.writerow(plunonce)

def main():
	# Short VP coordintation singular (with faulty inflection)
	vpsing = """ 
	S -> NP VP
	S -> NP VPfl
	NP -> Det Nsi
	VP -> Vsi cc Vsi2
	VPfl -> Vsi cc Vpl2
	VP -> Vsi2 cc Vsi
	VPfl -> Vsi2 cc Vpl
	Det -> 'in'
	cc -> 'en'
	Nsi -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	Vsi -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit'
	Vsi2 -> 'is lang' | 'is koart' | 'is âld' | 'is jong'
	Vpl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige'
	Vpl2 -> 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	# Short VP coordintation plural (with faulty inflection)
	vppl = """ 
	S -> NP VP
	S -> NP VPfl
	NP -> Det Npl
	VP -> Vpl cc Vpl2
	VPfl -> Vpl cc Vsi2
	VP -> Vpl2 cc Vpl
	VPfl -> Vpl2 cc Vsi
	Det -> 'de'
	cc -> 'en'
	Npl -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	Vsi -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit'
	Vsi2 -> 'is lang' | 'is koart' | 'is âld' | 'is jong'
	Vpl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige'
	Vpl2 -> 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	# Nonce sentences singular 
	vpsingnonce = """ 
	S -> NP VP
	S -> NP VPfl
	NP -> Det Nsi
	VP -> VsiR cc Vsi
	VPfl -> VsiR cc Vpl
	Det -> 'in'
	cc -> 'en'
	Vsi -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	Vpl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	# Nonce sentences plural
	vpplurnonce = """ 
	S -> NP VP
	S -> NP VPfl
	NP -> Det Npl
	VP -> VplR cc Vpl
	VPfl -> VplR cc Vsi
	Det -> 'de'
	cc -> 'en'
	Vsi -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	Vpl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	corsing, flsing = createLists(vpsing)
	shortVP_sing = list(zip(corsing, flsing))
	corplur, flplur = createLists(vppl)
	shortVP_plur = list(zip(corplur, flplur))

	# Get random words
	NounSing = get_words("newRandomWords/shortVP/shortVPSingularNouns2804.csv")
	NounPlur = get_words("newRandomWords/shortVP/shortVPPluralNouns2804.csv")
	Verbs2Sing = get_words("newRandomWords/shortVP/shortVPSingularVerbs2804.csv")
	Verbs2Plur = get_words("newRandomWords/shortVP/shortVPPluralVerbs2804.csv")

	# Create nonce sentences singular
	noncesing = addToGram(NounSing, vpsingnonce, "Nsi")
	noncesing = addToGram(Verbs2Sing, noncesing, "VsiR")
	noncesing, noncesingfl = createLists(noncesing)
	shortVP_nonceSing = list(zip(noncesing, noncesingfl))
	
	nonceplur = addToGram(NounPlur, vpplurnonce, "Npl")
	nonceplur = addToGram(Verbs2Plur, nonceplur, "VplR")
	nonceplur, nonceplurfl = createLists(nonceplur)
	shortVP_noncePlur = list(zip(nonceplur, nonceplurfl))

	writeTSV(shortVP_sing, shortVP_plur, shortVP_nonceSing, shortVP_noncePlur, "short_VP", "shortVPsing", "shortVPplur", "shortVPsingNonce", "shortVPplurNonce")
if __name__ == '__main__':
	main()

















