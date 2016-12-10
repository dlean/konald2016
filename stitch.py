import nltk
import random

# DOWNLOADED:
# maxent_treebank_pos_
# average perceptron tagger
# punkt tokenizer

verb = ['like', 'hate', 'would destroy', 'raise the roof like', 'care about', 'have thought a lot about', 'try to avoid', 'crave']
adj = ['disgusting', 'wonderful', 'triumphant', 'delicious', 'luscious', 'deformatory', 'wholesome', 'pure', 'insidious']
need = ['needed', 'not needed', 'abolished', 'encouraged']
beginning = ['No doubt', 'To be honest', 'Truthfully', 'Admittedly', 'I must say', 'Just kidding', 'Believe me']
fully = ['rightfully', 'wrongfully']

# This function displays the first character of the sentence with its POS tag
def pos_tag(sentence):
	text = nltk.word_tokenize(sentence)
	return (nltk.pos_tag(text))

def make_sentence_user_input(s, noun):
	if pos_tag(s)[0][1] == 'DT' or pos_tag(s)[0][1] == 'PRP' or pos_tag(s)[0][1] == 'PRP$' or pos_tag(s)[0][1] == 'NNP' or pos_tag(s)[0][1] == 'NN':
		print ("I %s %s because %s" % (random.choice(verb), noun, s.lower()))

	elif pos_tag(s)[0][1] == 'CC':
		print ("%s, %s is %s %s %s" % (random.choice(beginning), noun, random.choice(fully), random.choice(need), s.lower()))

	elif pos_tag(s)[0][1] == 'IN':
		print ("I %s %s %s" % (random.choice(verb), noun, s.lower()))

	elif pos_tag(s)[0][1] == 'VB':
		print ("To be honest, %s are %s so %s" % (noun, random.choice(adj), s.lower()))

	elif pos_tag(s)[0][1] == 'RB':
		print ("Better %s %s %s" % (random.choice(verb), noun, s.lower()))

	elif pos_tag(s)[0][1] == 'VBG':
		print ("%s are %s" % (noun, s.lower()))

	elif pos_tag(s)[0][1] == 'MD':
		print ("%s %s" % (noun, s.lower()))

	else:
		print(s)
