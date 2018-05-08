import sys
import os

import string_gen as STRS
import cracker as CRK
import reduction as RED


REPS = 10
ALPH_FILE = 'alph_file.txt'
PW_LEN = 3
NUM_PWS = 10	
WORDS = STRS.all_words_of_len(PW_LEN)
WORDSS = STRS.all_words_of_len(PW_LEN+1)
ALPH_CAPS = STRS.alphabet_ul() #len: 52
ALPH_CAPS_DIGS = STRS.alphabet_uld() #len: 62
ALPH_CAPS_DIGS_SP = STRS.alphabet_ulds() #len: 93

def sanitize(xs, l):
	temp = xs.split("'")
	temp.pop(0)
	temp.pop(-1)
	return list(filter(lambda x: len(x) is l, temp))

if len(sys.argv) < 2:
	print('no alphabet file provided...')
	resp = raw_input("are you sure you want to generate new alphabet file? (Y/n) ")
	if resp is not 'Y':
		sys.exit()
	s = 'rm '+ALPH_FILE
	os.system(s)
	with open(ALPH_FILE, 'a') as f:
		f.write('all_alph_perms:')
		f.write('\n')
		aap = STRS.perms_from_of_len(ALPH_CAPS, PW_LEN)
		f.write(aap)
		f.write('\n')
		f.write('all_perms_caps_digs:')
		f.write('\n')
		apcd = STRS.perms_from_of_len(ALPH_CAPS_DIGS, PW_LEN+1)
		f.write(apcd)
		f.write('\n')
		f.write('all_perms_caps_digs_sp:')
		f.write('\n')
		apcds = STRS.perms_from_of_len(ALPH_CAPS_DIGS_SP, PW_LEN+1)
		f.write(apcds)
		f.write('\n')
		print('run again with new alphabet file as lone command line arg')
		sys.exit()
else:
	with open(sys.argv[-1]) as f:
		data = f.readlines()
		try:
			aap = data[data.index('all_alph_perms:\n') + 1]
			apcd = data[data.index('all_perms_caps_digs:\n') + 1]
			apcds = data[data.index('all_perms_caps_digs_sp:\n') + 1]
		except Exception as e:
			print('something went wrong... possible with the argument file')
			sys.exit(e)

		print('loading word permutations from file...')
		aap = sanitize(aap, PW_LEN)
		apcd = sanitize(apcd, PW_LEN+1)
		apcds = sanitize(apcds, PW_LEN+1)
		print('done')

print('permuting word lists...')
STRS.permute(aap)
STRS.permute(apcd)
STRS.permute(apcds)
print('done')

# sanity check
assert('aaa' in aap)
assert('AAA' in aap)

print('3 letter search space size w/ caps: '+str(len(aap)))
print('4 letter search space size w/ caps and digits: '+str(len(apcd)))
print('4 letter search space size w/ caps, digits, and special: '+str(len(apcds)))

print('num permutations of alph with caps: '+str(len(aap)))
Aap = list(filter(RED.first_cap, aap))
print('num first cap permutations: '+str(len(Aap)))
aap_lower = list(filter(RED.all_lower, aap))
print('num all lower permutations: '+str(len(aap_lower)))
aap_any_cap = list(filter(RED.any_single_cap, aap))
print('num any cap permutations: '+str(len(aap_any_cap)))
AAP = list(filter(RED.all_upper, aap))
print('num all cap permutations: '+str(len(AAP)))
print('3 character dictionaries generated')

apcdn = list(filter(RED.last_is_digit, apcd))
print('num permutations with tail digit: '+str(len(apcdn)))
apcd1 = list(filter(RED.last_is_1, apcdn))
print('num permutations with tail 1: '+str(len(apcd1)))
Apcd1 = list(filter(RED.first_cap, apcd1))
print('num nonword likely passwords: '+str(len(Apcd1)))
APcd1_leet = RED.leet_filter(Apcd1, WORDS)
print('num leet password guesses: '+str(len(APcd1_leet)))
print(APcd1_leet)
print('4 character dictionaries generated')

bl3a,bfc3a,bac3a,baa3a = 0,0,0,0
il3a,ifc3a,iac3a,iaa3a = 0,0,0,0
words_dif,Words_dif,wOrDs_dif,WORDS_dif = 0,0,0,0

blb = 0
ilb = 0
for i in range(0, REPS):
	p = STRS.pw_suite(WORDS, NUM_PWS, STRS, RED, aap)
	base_lower3_speed = CRK.crack_speed(p['words'], aap)
	bl3a += base_lower3_speed
	print("base cracking speed (3 chars no caps): " + str(base_lower3_speed))
	base_fc3_speed = CRK.crack_speed(p['Words'], aap)
	bfc3a += base_fc3_speed
	print("first cap cracking speed (3 chars): " + str(base_fc3_speed))
	base_ac3_speed = CRK.crack_speed(p['wOrDs'], aap)
	bac3a +=  base_ac3_speed
	print("any one cap cracking speed (3 chars): " + str(base_ac3_speed))
	base_aa3_speed = CRK.crack_speed(p['WORDS'], aap)
	baa3a += base_aa3_speed
	print("any up to all cap cracking speed (3 chars): " + str(base_aa3_speed))

	imp_lower3_speed = CRK.crack_speed(p['words'], aap_lower)
	il3a += imp_lower3_speed
	print("improved cracking speed (3 chars no caps): " + str(imp_lower3_speed))
	imp_fc3_speed = CRK.crack_speed(p['Words'], Aap)
	ifc3a += imp_fc3_speed
	print("improved first cap cracking speed (3 chars): " + str(imp_fc3_speed))
	imp_ac3_speed = CRK.crack_speed(p['wOrDs'], aap_any_cap)
	iac3a += imp_ac3_speed
	print("improved any one cap cracking speed (3 chars): " + str(imp_ac3_speed))
	imp_aa3_speed = CRK.crack_speed(p['WORDS'], aap_any_cap+Aap+aap_lower+aap)
	iaa3a += imp_aa3_speed
	print("improved any up to all cap cracking speed (3 chars): " + str(imp_aa3_speed))

	leet_base = CRK.crack_speed(p['W0rds1'], apcds)
	blb += leet_base
	print("base crack speed for l337 passwords: "+str(leet_base))

	l = list(map(RED.leetify, APcd1_leet))
	leet_imp = CRK.crack_speed(p['W0rds1'], l+apcds)
	ilb += leet_imp
	print("improved crack speed for l337 passwords: "+str(leet_imp))

bl3a /= float(REPS) 
bfc3a /= float(REPS) 
bac3a /= float(REPS) 
baa3a /= float(REPS) 
il3a /= float(REPS) 
ifc3a /= float(REPS) 
iac3a /= float(REPS) 
iaa3a /= float(REPS) 

blb /= float(REPS)
ilb /= float(REPS)

print('...')
print('bl3a av speed: '+str(bl3a))
print('il3a av speed: '+str(il3a))

print('bac3a av speed: '+str(bac3a))
print('iac3a av speed '+str(iac3a))

print('bfc3a av speed: '+str(bfc3a))
print('ifc3a av speed: '+str(ifc3a))

print('baa3a av speed: '+str(baa3a))
print('iaa3a av speed: '+str(iaa3a))

print('...')

print('blb: '+str(blb))
print('ilb: '+str(ilb))

print('...')
print('cleaning up')
sys.exit()