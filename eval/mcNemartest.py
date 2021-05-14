# Adapted from: https://machinelearningmastery.com/mcnemars-test-for-machine-learning/
from statsmodels.stats.contingency_tables import mcnemar
import sys

def getLists(data, l):
	# Gets predictions from results
	for line in data:
		if line.startswith("True") or line.startswith("False"):
			items = line.split(" ")
			label = items[0].strip()
			l.append(label)
	return(l)

def ctabnum(model1list , model2list):
	# Gets numbers for contingency table
	c1c2 = c1i2 = i1c2 = i1i2 = 0
	for m1i, m2i in zip(model1list, model2list):
		if m1i == "True" and m2i == "True":
			c1c2 = c1c2 + 1
		elif m1i == "True" and m2i == "False":
			c1i2 = c1i2 + 1
		elif m1i == "False" and m2i == "True":
			i1c2 = i1c2 + 1
		else:
			i1i2 = i1i2 + 1
	return c1c2, c1i2, i1c2, i1i2

def main():
	model1 = sys.argv[1]
	model2 = sys.argv[2]
	m1L = []
	m2L = []

	m1 = open(model1, "r")
	m2 = open(model2, "r")
	model1list = getLists(m1, m1L)
	model2list = getLists(m2, m2L)


	c1c2, c1i2, i1c2, i1i2 = ctabnum(model1list, model2list)

	# These numbers should be the same
	print(len(model1list))
	print(len(model2list))
	print(c1c2 + c1i2 + i1c2 + i1i2)
	table = [[c1c2,c1i2],[i1c2,i1i2]]
	result = mcnemar(table, exact = True)
	print(f"statistic: {result.statistic} p-value: {result.pvalue}")
	alpha = 0.05
	if result.pvalue > alpha:
		print('Fail to reject H0')
	else:
		print('Reject H0')


if __name__ == '__main__':
	main()