from nltk import CFG
import nltk
from nltk.parse.generate import generate
import pandas as pd


def main():

	# simple NPI (Vpartic -> participle/voltooid deelwoord)
	npi = """
	S -> NP aux VP
	NP -> neg Nsi
	aux -> 'heeft'
	VP -> npi adj Vpartic
	aux -> 'is'
	neg -> 'gjin'
	npi -> 'ea'
	"""

	# npi across rel clause
	npiRel = """
	S -> NP aux VP
	NP -> neg Nsi RelCl
	NP -> Det Nsi Relcl
	RelCl -> adp Detpl Npl Vpl
	Vp -> npi adj Vpartic
	aux -> 'is'
	Det -> 'de'
	Detpl -> 'in'
	adp -> 'wêrfan'
	npi -> 'ea'
	""" 

if __name__ == '__main__':
	main()
