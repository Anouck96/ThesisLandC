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
	N -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
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
	N -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	"""

	# NPI with 
	npiH = """
	S -> NP aux npi VP
	S -> NP aux adj VP
	NP -> det N
	VP -> adp V
	det -> 'de'
	npi -> 'net'
	adj -> 'wol'
	N -> 'minsken' | 'manlju' | 'heiten' | 'memmen' | 'froulju' | 'plysjes' | 'famkes' | 'jonges' | 'keningen'
	aux -> 'hoege'
	adp -> 'te'
	V -> 'sizze' | 'wolle' | 'gean' |'stean'
	"""

	past, pastfl = createLists(npiPAST)
	npiP = list(zip(past, pastfl))
	fut, futfl = createLists(npiFUT)
	npiF = list(zip(fut, futfl))
	hoege, hoegefl = createLists(npiH)
	npiHoege = list(zip(hoege, hoegefl))



if __name__ == '__main__':
	main()