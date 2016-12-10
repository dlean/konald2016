import markovify
import stitch
import mod_corpus

mod_corpus.PG13("kanye.txt", "cleanye.txt", clean_word='avocado')

# Create new  corpus with only first 501 lines of Trump corpus
mod_corpus.short_corpus(501, "trump_500", "trump.txt")

# Combine two corpi
mod_corpus.combine_corp('cleanye.txt','trump.txt', 'trumpye.txt')

# Now that combined + truncated corpi created, get raw text as string.
text_K = open("cleanye.txt", "r", encoding='utf8').read()
text_Tr = open("trump.txt", "r", encoding='utf8').read()
text_Tr500 = open("trump_500.txt", "r", encoding='utf8').read()
text_c = open("trumpye.txt", "r", encoding='utf8').read()


# Calculate the number of tokens, i.e. length of each corpus
def corp_len(text):
	length = 0
	for line in text:
		for word in line.strip().split():
			length += 1
	return length

k_len = corp_len(text_K)
tr_len = corp_len(text_Tr)

# Calculate type-token ratio of two corpuses
def TTR(text):
	types = {}
	tokens = corp_len(text)

	for line in text:
		for word in line.strip().split():
			if word in types:
				types[word] += 1
			else:
				types[word] = 1
	return len(types)/tokens

k_TTR = TTR(text_K)
Tr_TTR = TTR(text_Tr)

# Print adjusted ratios to see how different parameters affect output
def adjust_results():
	print ("The type-token ratio of the Kanye corpus is %s." % (k_TTR))
	print ("The type-token ratio of the Trump corpus is %s." % (Tr_TTR))
	print ("The weight adjusted by type-token ratio is %s : 1." % (k_TTR/Tr_TTR))
	print ("\n")
	print ("The length of the Kanye corpus is %s." % (k_len))
	print ("The length of the Trump corpus is %s." % (tr_len))
	print ("The weight adjusted by corpus length is %s : 1." % (k_len/tr_len))
	print ("\n")

#adjust_weight()

print ("RANT BOT AT WORK")
print ("------------------------------------")

# The following functions use different parameters and ratios; we will compare output

# 1:1 weight with original corpi
def one_to_one_combine(r, l, topic):
	model_K = markovify.Text(text_K)
	model_Tr = markovify.Text(text_Tr)

	model_combo = markovify.combine([model_K, model_Tr], [1, 1])

	for i in range(r):									# create this many sentences
		s = text_model.make_short_sentence(l)			# sentence has maximum 'l' characters
#		print(stitch.pos_tag(s))
		stitch.make_sentence_user_input(s, topic)	

# weight adjusted by corpus length or type-token ratio
def weight_adjusted_combine(r, l, topic, ratio):
	model_K = markovify.Text(text_K)
	model_Tr = markovify.Text(text_Tr)

	model_combo = markovify.combine([model_K, model_Tr], [ratio, 1])

	for i in range(r):
		s = text_model.make_short_sentence(l)
#		print(stitch.pos_tag(s))
		stitch.make_sentence_user_input(s, topic)

# combined models with 1:1 weight on 500-line Trump corpus
def truncated_trump_combine(r, l, topic):
	model_K = markovify.Text(text_K)
	model_Tr = markovify.Text(text_Tr500)

	model_combo = markovify.combine([model_K, model_Tr], [1, 1])

	for i in range(r):
		s = text_model.make_short_sentence(l)
#		print(stitch.pos_tag(s))
		stitch.make_sentence_user_input(s, topic)

# single model with combined corpus
def combined_corpus(r, l, topic):
	text_model = markovify.Text(text_c)

	for i in range(r):
		s = text_model.make_short_sentence(l)
#		print(stitch.pos_tag(s))
		stitch.make_sentence_user_input(s, topic)

# single model with combined corpus
def one_corpus(r, l, topic, text):
	text_model = markovify.Text(text)

	for i in range(r):
		s = text_model.make_short_sentence(l)		
#		print(stitch.pos_tag(s))
		stitch.make_sentence_user_input(s, topic)

# This function is called from cakePencil.py, taking user input saved in cgi to use in sentence generation
# Uncomment to get sample sentences with different parameters. Adjust number of sentences and sentence length as needed!
def generate_sentences(n):
	
	#weight_adjusted_combine(5, 140, n, k_TTR/Tr_TTR)
	#weight_adjusted_combine(25, 500, n, k_len/tr_len)
	#truncated_trump_combine(25, 500, n)
	#combined_corpus(1, 140, n)
	one_to_one_combine(1, 140, n)			# 1 sentence, max 140 characters
	one_corpus(1, 140, n, text_K)
	one_corpus(1, 140, n, text_Tr)



