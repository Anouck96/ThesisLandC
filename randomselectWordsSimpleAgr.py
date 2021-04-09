
import random
import pandas as pd


def PROPN(PROPNdf):
	num_ofPROPN = 8

	#Select only the ones that are proper names (so do not contain plural forms)
	PROPNdf['feats'] = PROPNdf.feats.apply(lambda x: x[1:-1].split(" "))
	namesdf = PROPNdf[PROPNdf['feats'].str.len() == 1]

	randomnames = namesdf.sample(n=num_ofPROPN)
	return randomnames

def NOUNS(NOUNdf):
	num_Nouns = 8

	 #Select singular nouns
	singNouns = (NOUNdf[NOUNdf.feats.str.contains("Number.Sing")])
	randomsingNouns = singNouns.sample(n=num_Nouns)

	# Select plural forms for selected nouns
	listOfsings = randomsingNouns['lemma'].to_list()

	allForms = (NOUNdf[NOUNdf['lemma'].isin(listOfsings)])
	pluralNouns = (allForms[allForms.feats.str.contains("Number.Plur")])

	return randomsingNouns, pluralNouns


def VERBS(VERBdf):
	num_verbs = 8
	#Select singular verbs
	singVerbs = (VERBdf[VERBdf.feats.str.contains("Person.Third Number.Sing")])
#	singThirdPVerbs = singVerbs[singVerbs.feats.str.contains("Person.Third")]

	randomsingVerbs = singVerbs.sample(n=num_verbs)

	#Select plural forms for selected verbs
	listOfsinVerbs = randomsingVerbs['lemma'].to_list()

	allVerbs = (VERBdf[VERBdf['lemma'].isin(listOfsinVerbs)])
	plThirdVB = allVerbs[allVerbs.feats.str.contains("Person.Third Number.Plur")]

	#pluralVB = (plThirdVB[plThirdVB.feats.str.contains("Number.Plur")])


	return randomsingVerbs, plThirdVB


def main():

	#Read in the tsv dictionary as a dataframe with the lemma, wordform and features
	df = pd.read_csv("forms2.tsv", sep="\t", names=["lemma", "word", "feats"])

	# Create new dataframe with words of certain pos
	PROPNdf = (df[df.feats.str.contains("PROPN")])
	NOUNdf = (df[df.feats.str.contains("Pos.NOUN")])
	VERBdf = (df[df.feats.str.contains("Pos.VERB")])
	
	randomPROPN = PROPN(PROPNdf)
	randomSingNouns, pluralNouns = NOUNS(NOUNdf)
	randomSingVerbs, pluralVB = VERBS(VERBdf)


	#Write different forms to file
	randomPROPN.to_csv(r'simpleAgrPROPN.csv', index=False)
	randomSingVerbs.to_csv(r'AgrSingVBs.csv', index=False)
	pluralVB.to_csv(r'AgrPluralVBs.csv', index=False)
	randomSingNouns.to_csv(r'AgrSingNOUN.csv', index=False)
	pluralNouns.to_csv(r'AgrPlNoun.csv', index=False)

if __name__ == '__main__':
	main()





















