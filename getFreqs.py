from collections import Counter
import glob

def main():
	allWords = []
	for filepath in glob.glob("*.projection"):
		fil = open(filepath, "r")
		for line in fil:
			if line[0].isdigit() and line[1] == "\t":
				line = line.split("\t")
				word = line[1][0].lower() + line[1][1:]
				tup = ((word, line[3]))
				if tup[0] == "rOOT":
					pass
				else:
					allWords.append(tup)
	counts = Counter(allWords)

	with open("counts.txt", "w") as f:
		for k,v in counts.most_common():
			f.write("{} {}\n".format(k,v))

if __name__ == '__main__':
	main()