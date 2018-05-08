from random import randint

LEET = {'E':3, 'e':3, 'O':0, 'o':0, 'A':4, 'a':'@', 'I':1, 
        'i':1, 'T':7, 't':7, 'Z':2, 'z':2, 'B':8, 'b':8, 'P':9, 'p':9,
        'S':'$', 's':'$', 'C':'<', 'c':'<'}

# many concessions were made here
REV_LEET = {'3':'e', '0':'o', '4':'a', '@':'a', '1':'i', '7':'t', '2':'z',
            '8':'b', '$':'s', '<':'c', '9':'p'}


def first_cap(w):
    return w[0].isupper() and w[1:].islower()

def any_single_cap(w):
	return (1 == len(list(filter(lambda x: x.isupper(), [c for c in w]))))

def all_lower(w):
	return (len(w) == len(list(filter(lambda x: x.islower(), [c for c in w]))))

def all_upper(w):
	return (len(w) == len(list(filter(lambda x: x.isupper(), [c for c in w]))))

def last_is_digit(w):
	return (w[-1].isdigit() and (len(list(filter(lambda x: x.isdigit(), w))) is 1))

def random_cap_in(w):
	x = randint(0,len(w)-1)
	return str(w[:x] + w[x].upper() + w[(x+1):])

def append_dig(w):
	wl = [1,2,3,4,5,6,7,8,9,0]
	return [w + str(i) for i in wl]

def leetify(w):
	new_word = ""
	for c in w:
		try:
			new_word += str(LEET[c])
		except Exception as e:
			new_word += c
	return new_word

def un_leetify(w):
	new_word = ""
	for c in w:
		try:
			new_word += str(REV_LEET[c])
		except Exception as e:
			new_word += c
	return new_word

def add_num(xs):
	return list(reduce(lambda x,y: x+y, list(map(append_dig, xs))))

def last_is_1(w):
	return str(w[-1]) == "1"

def add_fst_cap(xs):
	return [str(x[0].upper()) + str(x[1:]) for x in xs]

def all_cap(w):
	s = ""
	for c in w:
		s += c.upper()
	return s

def leet_filter(xs, words):
	d = {}
	for w in words:
		d[w] = w
	out = []
	for x in xs:
		try:
			temp = un_leetify(x[:-1]) # drop tailing number
			d[temp]
			out.append(x)
		except Exception as e:
			continue
	return out
#def leet(w):
#	yes = False
#	for c in w:
		
