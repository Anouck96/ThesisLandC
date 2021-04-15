import random
import pandas as pd

def getNouns(nr, NOUNdf):
	# Select singular nouns
	singNouns = (NOUNdf[NOUNdf.feats.str.contains("Number.Sing")])
	randomsingNouns = singNouns.sample(n=nr)
	randomsingNouns[~randomsingNouns.feats.str.contains("Number.Plur")]
	print(randomsingNouns)

	# Select plural forms for selected nouns
	listOfSings = randomsingNouns['lemma'].to_list()
	allForms = (NOUNdf[NOUNdf['lemma'].isin(listOfSings)])
	pluralNouns = (allForms[allForms.feats.str.contains("Number.Plur")])
	pl = pluralNouns.drop_duplicates(subset="lemma")
	print(pl)
	return randomsingNouns, pl


def main():
	df = pd.read_csv("forms2.tsv", sep="\t", names=["lemma", "word", "feats"])

	nr = 4
	# Create dataframes for specific POStags
	NOUNdf = (df[df.feats.str.contains("Pos.NOUN")])
	
	randomSingNouns , pluralNouns = getNouns(nr, NOUNdf)
	print(randomSingNouns.shape[0])
	print(pluralNouns.shape[0])
	while randomSingNouns.shape[0] != nr or pluralNouns.shape[0] != nr:
		randomSingNouns , pluralNouns = getNouns(nr, NOUNdf)
	else:
		pass

	# Write to files 
	randomSingNouns.to_csv(r'SimpleAgreementSingularNouns.csv', index=False)
	pluralNouns.to_csv(r'SimpleAgreementPluralNouns.csv', index=False)

if __name__ == '__main__':
	main()