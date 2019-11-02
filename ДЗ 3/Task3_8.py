from Bio.Seq import Seq

s = 'agatacaca'

Se = Seq(s)
Se.reverse_complement()

# Or:


def is_dna(string):
	n = True
	nucleotides = ['A', 'T', 'G', 'C']
	s = string.upper()
	for i in s:
		if i not in nucleotides:
			n = False
	return n

#########

def rev_method_1(string):
	s_rev_1 = string[::-1]
	return s_rev_1


def rev_method_2(string):
	s_rev_2 = ''.join(reversed(string))
	return s_rev_2


def rev_method_3(string):
	lett_list = []
	for lett in string:
		lett_list.append(lett)
	lett_list.reverse()

	s_rev_3 = ''
	for i in lett_list:
		s_rev_3 += i
	return s_rev_3

#########


def complement_method_1(string):
	s_new = ''
	s = string.upper()
	for i in s:
		if i == 'A':
			s_new += 'T'
		elif i == 'T':
			s_new += 'A'
		elif i == 'G':
			s_new += 'C'
		elif i == 'C':
			s_new += 'G'
	return s_new


def complement_method_2(string):
	s_new = ''
	changes = {'a': 'T', 't': 'A', 'g': 'C', 'c': 'G'}
	s = string.lower()
	for i in s:
		if i in changes.keys():
			s_new += changes[i]
	return s_new


# Types of rev_comp's:


def rev_comp_1(string):
	if is_dna(string):
		str1 = rev_method_1(string)
		str2 = complement_method_1(str1)
		return str2
	else:
		print('Sorry, it is not DNA.')


def rev_comp_2(string):
	if is_dna(string):
		str1 = rev_method_2(string)
		str2 = complement_method_1(str1)
		return str2
	else:
		print('Sorry, it is not DNA.')


def rev_comp_3(string):
	if is_dna(string):
		str1 = rev_method_3(string)
		str2 = complement_method_1(str1)
		return str2
	else:
		print('Sorry, it is not DNA.')


def rev_comp_4(string):
	if is_dna(string):
		str1 = rev_method_1(string)
		str2 = complement_method_2(str1)
		return str2
	else:
		print('Sorry, it is not DNA.')


def rev_comp_5(string):
	if is_dna(string):
		str1 = rev_method_2(string)
		str2 = complement_method_2(str1)
		return str2
	else:
		print('Sorry, it is not DNA.')


def rev_comp_6(string):
	if is_dna(string):
		str1 = rev_method_3(string)
		str2 = complement_method_2(str1)
		return str2
	else:
		print('Sorry, it is not DNA.')
