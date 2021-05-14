import random
import sys

def main():

	name = sys.argv[2]
	counts = int(sys.argv[1])
	half = int(counts/2)
	ct = ["True"] * half
	ct2 = ["False"] * half
	ct.extend(ct2)
	random.shuffle(ct)


	with open(name, "w") as f:
		for item in ct:
			f.write(item + "\n")

if __name__ == '__main__':
	main()