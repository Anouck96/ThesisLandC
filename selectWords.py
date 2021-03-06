import random
import pandas as pd


def getPROPN(nr, PROPNdf):

	#Select only the ones that are proper names (so do not contain plural forms)
	PROPNdf['feats'] = PROPNdf.feats.apply(lambda x: x[1:-1].split(" "))
	namesdf = PROPNdf[PROPNdf['feats'].str.len() == 1]

	randomnames = namesdf.sample(n=nr)
	return randomnames

def getNouns(nr, NOUNdf):
	# Select singular nouns
	singNouns = (NOUNdf[NOUNdf.feats.str.contains("Number.Sing")])
	sg = singNouns[~singNouns.feats.str.contains("Number.Plur")]
	randomsingNouns = sg.sample(n=nr)

	# Select plural forms for selected nouns
	listOfSings = randomsingNouns['lemma'].to_list()
	allForms = (NOUNdf[NOUNdf['lemma'].isin(listOfSings)])
	pluralNouns = (allForms[allForms.feats.str.contains("Number.Plur")])
	pn = pluralNouns[~pluralNouns.feats.str.contains("Number.Sing")]
	pl = pn.drop_duplicates(subset="lemma")
	return randomsingNouns, pl


def getVerbs(nr, VERBdf):
	# Select singular verbs
	singVerbs = (VERBdf[VERBdf.feats.str.contains("Number.Sing")])
	sgV = singVerbs[~singVerbs.feats.str.contains("Number.Plur")]
	randomsingVerbs = singVerbs.sample(n=nr)

	# Select plural forms for selected nouns
	singVerbslist = randomsingVerbs['lemma'].to_list()
	allFormsV = (VERBdf[VERBdf['lemma'].isin(singVerbslist)])
	pluralVerbs = (allFormsV[allFormsV.feats.str.contains("Number.Plur")])
	pv = pluralVerbs[~pluralVerbs.feats.str.contains("Number.Sing")]
	plurVerbs = pv.drop_duplicates(subset="lemma")
	return randomsingVerbs, plurVerbs


def main():
	df = pd.read_csv("forms2.tsv", sep="\t", names=["lemma", "word", "feats"])

	nr = 4
	# Create dataframes for specific POStags
	PROPNdf = (df[df.feats.str.contains("PROPN")])
	NOUNdf = (df[df.feats.str.contains("Pos.NOUN")])
	VERBdf = (df[df.feats.str.contains("Pos.VERB")])
	VERBTdf = (VERBdf[VERBdf.feats.str.contains("Person.Third")])
	ADPdf = (df[df.feats.str.contains("Pos.ADP")])
	ADJdf = (df[df.feats.str.contains("Pos.ADJ")])
	VERBINFdf = (df[df.feats.str.contains("VerbForm.Inf")])
	randomADP = ADPdf.sample(n=nr)
	randomADJ = ADJdf.sample(n=nr)
	randomInfVB = VERBINFdf.sample(n=nr)

	randompropn = getPROPN(nr, PROPNdf)

	randomSingNouns , pluralNouns = getNouns(nr, NOUNdf)
	randomSingVerbs, pluralVerbs = getVerbs(nr, VERBTdf)

	#Check if for both there are nr items
	while randomSingNouns.shape[0] != nr or pluralNouns.shape[0] != nr:
	 	randomSingNouns , pluralNouns = getNouns(nr, NOUNdf)
	else:
	 	pass

	while randomSingVerbs.shape[0] != nr or pluralVerbs.shape[0] != nr:
		randomSingVerbs, pluralVerbs = getVerbs(nr, VERBdf)
	else:
		pass


	# Write to files 
	randompropn.to_csv(r'propn.csv', index=False)
	randomSingNouns.to_csv(r'singNoun.csv', index=False)
	pluralNouns.to_csv(r'plurNoun.csv', index=False)
	randomSingVerbs.to_csv(r'singVerb.csv', index=False)
	pluralVerbs.to_csv(r'plurVerb.csv', index=False)
	randomADJ.to_csv(r'adj.csv', index=False)
	randomInfVB.to_csv(r'infVerb.csv', index=False)
	randomADP.to_csv(r'adp.csv', index=False)

if __name__ == '__main__':
	main()











