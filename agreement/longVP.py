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

def writeTSV(sing, plu, singNonce, pluNonce, mainName, s, p, sn, pn):
	with open("longVP_data.tsv", "w") as out_file:
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


def main():

	# Long VP coordination singular (with faulty inflection)
	longVpCor = """ 
	S -> NP VPs cc V
	S -> NP VPs cc Vpl
	NP -> D Nsi
	D -> 'in'
	cc -> 'en'
	Nsi -> 'mins' | 'man' | 'heit' | 'mem' | 'frou' | 'plysje' | 'famke' | 'jonge' | 'kening'
	VPs -> 'sjocht graach televyzjeshows' | 'kin in protte ferskillende talen' | 'is trijeentweintich jier âld' | "spilet graach tennis mei kollega's" | 'skriuwt alle dagen yn in sjoernaal'
	V -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	Vpl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	# Nonce Variant on "skriuwt yn in sjoernaal"
	longVPsingNonce = """
	S -> NP VPS cc V
	S -> NP VPS cc Vpl
	NP -> D Nsi
	D -> 'in'
	cc -> 'en'
	VPS -> v adp D N
	V -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	Vpl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""


	# Long VP coordination plural (with faulty inflection)
	longVpCorpl = """ 
	S -> NP VPpl cc Vpl
	S -> NP VPpl cc V
	NP -> D Npl
	cc -> 'en'
	Npl -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	VPpl -> 'kinne in protte ferkillende talen' | 'wolle graach televyzjeshows sjen' | 'binne trijeentweintich jier âld' | "spylje graach tennis mei kollega's" | 'skriuwe alle dagen yn in sjoernaal'
	V -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	Vpl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	D -> 'de'
	"""

	# Nonce Variant on "skriuwt yn in sjoernaal" plural
	longVPplurNonce = """
	S -> NP VPS cc Vpl
	S -> NP VPS cc V
	NP -> D Npl
	D -> 'de'
	cc -> 'en'
	VPS -> v adp D N
	V -> 'hat' | 'kin' | 'komt' | 'wit' | 'set' | 'leit' | 'is lang' | 'is koart' | 'is âld' | 'is jong'
	Vpl -> 'hawwe' | 'kinne' | 'komme' | 'witte' | 'sette' | 'lige' | 'benne lang' | 'benne koart' | 'benne âld' | 'benne jong'
	"""

	longVPsg, longVPsgfl = createLists(longVpCor)
	longVP_sing = list(zip(longVPsg, longVPsgfl))
	
	longVPpl, longVPplfl = createLists(longVpCorpl)
	longVP_plur = list(zip(longVPpl, longVPplfl))


# Get random words
	NounSing = get_words("newRandomWords/longVP/longVPSingularNouns3004.csv")
	NounPlur = get_words("newRandomWords/longVP/longVPPluralNouns3004.csv")
	NounSing2 = get_words("newRandomWords/longVP/longVPSingular2Nouns3004.csv")
	NounPlur2 = get_words("newRandomWords/longVP/longVPPlural2Nouns3004.csv")
	VerbSing = get_words("newRandomWords/longVP/longVPSingularVerbs3004.csv")
	VerbPlural = get_words("newRandomWords/longVP/longVPPluralVerbs3004.csv")
	ADP = get_words("newRandomWords/longVP/longVPADP3004.csv")


# Add to grammar and create minimal pairs
	noncesing = addToGram(NounSing, longVPsingNonce, "Nsi")
	noncesing = addToGram(VerbSing, noncesing, "v")
	noncesing = addToGram(ADP, noncesing, "adp")
	noncesing = addToGram(NounSing2, noncesing, "N")
	nonces, noncesingfl = createLists(noncesing)
	longVP_noncesing = list(zip(nonces, noncesingfl))

	nonceplur = addToGram(NounPlur, longVPplurNonce, "Npl")
	nonceplur = addToGram(VerbPlural, nonceplur, "v")
	nonceplur = addToGram(ADP, nonceplur, "adp")
	nonceplur = addToGram(NounPlur2, nonceplur, "N")
	noncep, noncepfl = createLists(nonceplur)
	longVP_nonceplur = list(zip(noncep, noncepfl))


	writeTSV(longVP_sing, longVP_plur, longVP_noncesing, longVP_nonceplur, "longVP", "longVP_sg", "longVP_pl", "longVP_sgNonce", "longVP_plNonce")

if __name__ == '__main__':
	main()