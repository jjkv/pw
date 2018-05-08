import itertools
from nltk.corpus import words
from random import shuffle

# from OWASP special character index (backslash ommitted)
PW_SPECIAL = [' ','!','"','#','$','%','&','(',')','*','+',",",'-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']

def permute(xs):
	shuffle(xs)

def all_words():
	return words.words()

def all_words_of_len(n):
	word_list = words.words()
	return list(filter(lambda x: len(x) is n, word_list))

def l_from_to(a, b):
	return [chr(i) for i in range(ord(a), ord(b)+1)]

def lowers():
	return l_from_to('a','z')

def digits():
	return l_from_to('0','9')

def uppers():
	return l_from_to('A','Z')

def special():
	return PW_SPECIAL

def alphabet_ul():
	return list(uppers() + lowers())

def alphabet_uld():
	return list(uppers() + lowers() + digits())

def alphabet_ulds():
	return list(uppers() + lowers() + digits() + special())

def perms_from_of_len(a, n):
	tups = list(itertools.product(a, repeat = n))
	return list(map(lambda x: ''.join(x), tups))

def select_random_from(xs, n):
	permute(xs)
	return list(map(lambda x: x.lower(), xs[:n]))

def words_and_not_words(xs, ws):
	flwD = {}
	for w in ws:
		flwD[w] = w

	words, not_words = [],[]
	for x in xs:
		try:
			words.append(flwD[x])
		except KeyError:
			not_words.append(x)

	return words, not_words

def pw_suite(w, n, S, R, spc):

	#print('num '+str(PW_LEN)+' char words: '+str(len(WORDS)))
	pblah = S.select_random_from(spc, n)
	passwords = S.select_random_from(w, n)
	Passwords = R.add_fst_cap(passwords)
	pAsSwOrDs = list(map(R.random_cap_in, passwords))
	PASSWORDS = list(map(R.all_cap, passwords))
	passwords1 = R.add_num(passwords)
	Passwords1 = R.add_fst_cap(passwords1)
	Passwords1_prob = list(filter(lambda x: x[-1] is "1", Passwords1))
	print(len(Passwords1_prob))
	P4sswords1 = list(map(R.leetify, Passwords1_prob))
	print(str(len(P4sswords1))+' passwords generated')
	d = {'words':passwords, 'Words':Passwords, 'wOrDs':pAsSwOrDs, 'WORDS':PASSWORDS, 
	     'words1':passwords1, 'Words1':Passwords1, 'Words1_prob':Passwords1_prob, 
	     'W0rds1':P4sswords1, 'wblah':pblah}
	return d
