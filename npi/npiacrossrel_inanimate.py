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


def writeTSV(past, fu, mainName, p, f):
	with open("npiacrossrel_inanimate_data.tsv", "w") as out_file:
		tsv_output = csv.writer(out_file, delimiter='\t')

		# Write minimal pairs past
		for it in past:
			start = [mainName, p]
			start.extend(it)
			tsv_output.writerow(start)
	
		# Write minimal pairs future
		for i in fu:
			stplu = [mainName, f]
			stplu.extend(i)
			tsv_output.writerow(stplu)

def main():
# NPI PAST
	npiPAST = """
	S -> NP1 Rel VP
	S -> NP2 Rel VP
	NP1 -> neg N
	NP2 -> det N
	Rel -> sconj det Np Vrel
	VP -> aux npi adj Vpartic
	neg -> 'gjin'
	det -> 'de'
	N -> 'huzen' | "auto's" | 'boeken' | 'tafels' | 'dingen'
	sconj -> "dy't"
	Np -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	Vrel -> 'fan hâlde' | 'bewûnderje'
	aux -> 'benne'
	npi -> 'ea'
	adj -> 'populêr' | 'ferneamd' | 'earste' | 'goed' | 'moai'
	Vpartic -> 'west' """

# NPI FUTURE
	npiFUT = """
	S -> NP1 Rel VP
	S -> NP2 Rel VP
	NP1 -> neg N
	NP2 -> det N
	Rel -> sconj det Np Vrel
	VP -> aux npi adj Vpartic
	neg -> 'gjin'
	det -> 'de'
	N -> 'huzen' | "auto's" | 'boeken' | 'tafels' | 'dingen'
	Np -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	sconj -> "dy't"
	Vrel -> 'fan hâlde' | 'bewûnderje'
	aux -> 'sille'
	npi -> 'ea'
	adj -> 'populêr' | 'ferneamd' | 'earste' | 'goed' | 'moai'
	Vpartic -> 'wêze' """


	npiP, npiPfl = createLists(npiPAST)
	npi_PAST = list(zip(npiP, npiPfl))

	npiF, npiFfl = createLists(npiFUT)
	npi_FUT = list(zip(npiF, npiFfl))
	writeTSV(npi_PAST, npi_FUT, "npiacrossrel_inanimate", "PAST", "FUTURE")

if __name__ == '__main__':
	main()