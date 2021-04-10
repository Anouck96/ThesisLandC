from nltk import CFG
import nltk
from nltk.parse.generate import generate
import pandas as pd

def get_words(csvFile):
	df = pd.read_csv(csvFile, sep=",")
	list_of_words = df['word'].to_list()

	return list_of_words


def main():
	#Create grammar for singular nouns and singular PROPN

	Grammar = """
  S -> NP VP
  VP -> V 
  NP -> Det N
  NP -> Propn
  V -> "laughs" | "smiles"
  Det -> "the"
  N -> "author" | "pilot"
  """

	# grammarsing = CFG.fromstring("""
 #  S -> NP VP
 #  VP -> V 
 #  NP -> Det N
 #  NP -> Propn
 #  V -> "laughs" | "smiles"
 #  Det -> "the"
 #  N -> "author" | "pilot"
 #  """)

	# Create grammar for plural nouns
	grammarplur = CFG.fromstring("""
  S -> NP VP
  VP -> V
  NP -> Det N
  V -> "laugh"
  V -> "smile"
  Det -> "the"
  N -> "authors" | "pilots"
  """)

	#Get the lists of random words

	PROPNsing = get_words("simpleAgrPROPN.csv")
	#print(PROPNsing)

	NOUNsing = get_words("AgrSingNOUN.csv")
	#print(NOUNsing)

	NOUNpl = get_words("AgrPlNoun.csv")
	#print(NOUNpl)

	VERBsing = get_words("AgrSingVBs.csv")
	#print(VERBsing)

	VERBpl = get_words("AgrPluralVBs.csv")
	#print(VERBpl)


#	prod = grammarsing.productions()

	# Add rules to the string grammar for the Proper nouns
	print(Grammar)
	s = ""
	listOfpropn = []
	for propns in PROPNsing:
		print(propns)
		s = "Propn -> " + "'"+propns+"'"
		listOfpropn.append(s)

	print(listOfpropn)
	props = '\n'.join(listOfpropn)
	gr = Grammar + props
	print(gr)
	# Create CFG from the string
	sing = CFG.fromstring(gr)
	print(sing.productions())
	# Print the generated sentences
	for sent in generate(sing):
		print(' '.join(sent))

	# for item in PROPNsing:
	# 	item = "'"+item+"'"
	# 	lhs = nltk.grammar.Nonterminal('Propn')
	# 	rhs = nltk.grammar.Nonterminal(item)
	# 	new_production = nltk.grammar.Production(lhs, [rhs])
	# 	#print(new_production)
	# 	prod.append(new_production)


	#  #Generate n sentences
	# print(grammarsing)



	for sentence in generate(grammarsing):
		print(' '.join(sentence))
	# for sentence in generate(grammarplur):
	# 	print(' '.join(sentence))

	#Sentences with max depth
	# for sentenced in generate(grammar, depth=4):
	# 	print(' '.join(sentenced))

	# #Number of sentences without max depth
	# print(len(list(generate(grammar))))



if __name__ == '__main__':
	main()
 	
