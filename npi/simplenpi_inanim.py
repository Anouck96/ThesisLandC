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
	with open("simplenpi_inanimate_data.tsv", "w") as out_file:
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

	# simple NPI (PAST)
	npiPAST = """
	S -> NP1 aux VP
	S -> NP2 aux VP
	NP1 -> neg N
	NP2 -> det N
	aux -> 'benne'
	VP -> npi adj Vpartic
	neg -> 'gjin'
	det -> 'de'
	npi -> 'ea' 
	adj -> 'populêr' | 'ferneamd' | 'earste' | 'goed' | 'moai'
	Vpartic -> 'west'
	N -> 'huzen' | "auto's" | 'boeken' | 'tafels' | 'dingen'
	"""

	# simple NPI (FUTURE)
	npiFUT = """
	S -> NP1 aux VP
	S -> NP2 aux VP
	NP1 -> neg N
	NP2 -> det N
	aux -> 'sille'
	VP -> npi adj Vpartic
	neg -> 'gjin'
	det -> 'de'
	npi -> 'ea' 
	adj -> 'populêr' | 'ferneamd' | 'earste' | 'goed' | 'moai'
	Vpartic -> 'wêze'
	N -> 'huzen' | "auto's" | 'boeken' | 'tafels' | 'dingen'
	"""


	past, pastfl = createLists(npiPAST)
	npiP = list(zip(past, pastfl))
	fut, futfl = createLists(npiFUT)
	npiF = list(zip(fut, futfl))


	writeTSV(npiP, npiF, "simpleNPI_inanim", "PAST", "FUTURE")

if __name__ == '__main__':
	main()