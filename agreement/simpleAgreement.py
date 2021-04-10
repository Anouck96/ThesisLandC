from nltk import CFG
import nltk
from nltk.parse.generate import generate
import pandas as pd

def get_words(csvFile):
	df = pd.read_csv(csvFile, sep=",")
	list_of_words = df['word'].to_list()

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

def main():
	#Create grammar for singular nouns and singular PROPN (with faulty verb inflection)

	SingGrammar = """
  S -> NP VP
  VP -> VSing
  VP -> VPl
  NP -> Det N
  NP -> Propn
  Det -> 'in'"""

	# Create grammar for plural nouns (with faulty verb inflection)
	PlurGrammar = """
  S -> NP VP
  VP -> VPl
  VP -> VSing
  NP -> Det Npl
  Det -> 'de'"""

	#Get the lists of random words
	PROPNsing = get_words("simpleAgrPROPN.csv")

	NOUNsing = get_words("AgrSingNOUN.csv")

	NOUNpl = get_words("AgrPlNoun.csv")

	VERBsing = get_words("AgrSingVBs.csv")

	VERBpl = get_words("AgrPluralVBs.csv")

	# Add rules to the singular Grammar
	gr = addToGram(PROPNsing, SingGrammar, "Propn")
	gr = addToGram(NOUNsing, gr, "N")
	gr = addToGram(VERBsing, gr, "VSing")
	gr = addToGram(VERBpl, gr, "VPl")

	# Create CFG from the string
	sing = CFG.fromstring(gr)

	# Print the generated sentences
	for sent in generate(sing):
		print(' '.join(sent))

	# Add rules to the plural grammar
	grpl = addToGram(NOUNpl, PlurGrammar, "Npl")
	grpl = addToGram(VERBpl, grpl, "VPl")
	grpl = addToGram(VERBsing, grpl, "VSing")

	#Create CFG for plural grammar
	plur = CFG.fromstring(grpl)

	#Print generated sentences
	for se in generate(plur):
		print(' '.join(se))

if __name__ == '__main__':
	main()
 	
