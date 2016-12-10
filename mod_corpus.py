

# This function looks for inappropriate words in a certain corpus, 
# replaces such words with a word of the user's choice, then prints to a new file

def PG13(original, outname, clean_word='****'):

	f = open('swear.txt', 'r', encoding='utf8')
	f1 = open(original, 'r', encoding='utf8')
	f2 = open(outname, 'w', encoding='utf8')

	bad = [word for line in f for word in line.split()]

	for line in f1:
		for word in line.split():
			if word.lower() in bad:
				f2.write(clean_word + " ")
			else:
				f2.write(word + " ")


# Takes first n lines of corpus and copies to new file
def short_corpus(n, outname, inname):
	i = 0
	with open(outname, 'w', encoding='utf8') as f:
		with open(inname, "r", encoding='utf8') as f1:
			for line in f1:
				if i < n:
					f.write(line)
					i = i + 1


# Concatenates two texts
def combine_corp(t1, t2, outname):
	filenames = [t1, t2]

	with open(outname, 'w', encoding='utf8') as outf:
		for txt in filenames:
			with open(txt, "r", encoding='utf8') as inf:
				for line in inf:
					outf.write(line)