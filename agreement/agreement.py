from nltk import CFG
import nltk
from nltk.parse.generate import generate
import pandas as pd

def main():

	# Agreement in sentential complement sing NP (with faulty inflection)
	sent_comp = """
	S -> NP VP Cp 
	NP -> Det Nsi
	VP -> Vsi
	Cp -> cc Vpcomp
	VPcomp -> Det Nsi Vsi
	Vpcomp -> Det Nsi Vpl
	Det -> 'in"""

	# Agreement in sentential complement plural NP (with faulty inflection)
	sent_comppl = """
	S -> NP VP Cp 
	NP -> Det Nsi
	VP -> Vsi
	Cp -> sconj Vpcomp
	VPcomp -> Det Npl Vpl
	Vpcomp -> Det Npl Vsi
	Det -> 'de'
	sconj -> 'dat'
	"""

	# Agreement across a prepositional phrase singular noun (with faulty inflections)
	prep = """ 
	S -> NP VP
	NP -> NP PP
	NP -> Det Nsi
	PP -> adp det Npl
	VP -> Vsi
	VP -> Vpl
	"""

	# Agreement across a prepositional phrase plural noun (with faulty inflections)
	preppl = """ 
	S -> NP VP
	NP -> NP PP
	NP -> Det Nsi
	PP -> adp det Npl
	VP -> Vpl
	VP -> Vsi
	"""

	# Across subject relative clause (singular noun + faulty inflection)
	sub_rel = """
	S -> NP VP
	NP -> NP RelClause
	NP -> Det Nsi
	RelClause -> sconj VPrel
	sconj -> 'dy'
	VPrel -> Vsi Det Nsi
	VP -> Vsi
	VP -> Vpl 
	Det -> 'in"""

	# Across subject relative clause (plural noun + faulty inflection)
	sub_relpl = """
	S -> NP VP
	NP -> NP RelClause
	NP -> Det Npl
	RelClause -> sconj VPrel
	sconj -> 'dy'
	VPrel -> Vpl Det Nsi
	VP -> Vpl
	VP -> Vsi
	Det -> 'de' """

	# Short VP coordintation singular (with faulty inflection)
	vpCor = """ 
	S -> NP VP
	NP -> Det Nsi
	VP -> Vsi cc Vsi
	Vp -> Vsi cc Vpl
	Det -> 'in'
	cc -> 'en'
	"""

	# Short VP coordintation plural (with faulty inflection)
	vpCorpl = """ 
	S -> NP VP
	NP -> Det Npl
	VP -> Vpl cc Vsi
	Vp -> Vpl cc Vpl
	Det -> 'de'
	cc -> 'en' 
	"""

	# Long VP coordination singular (with faulty inflection)
	longVpCor = """ 
	S -> NP VPsi cc VP
	NP -> D Nsi
	#VP -> V obj
	VP -> Vpsi
	VP -> Vppl
	VPsi -> "knows many different languages"
	VPpl -> "know many different langauges"
	D -> 'in'
	"""
	# Long VP coordination plural (with faulty inflection)
	longVpCorpl = """ 
	S -> NP VPpl cc VP
	NP -> D Npl
	#VP -> V obj
	VP -> Vppl
	VP -> Vpsi
	VPsi -> "knows many different languages"
	VPpl -> "know many different langauges"
	D -> 'de'
	"""

	# across object relative clause (singular noun + faulty inflection)
	objrel = """ 
	S -> NP VP
	NP -> Det Nsi NPcomp
	NPcomp -> adp Detpl Npl Vpl
	VP -> Vsi
	VP -> Vpl
	Det -> 'in'
	Detpl -> 'de'
	adp -> 'wêrfan"""

	# across object relative clause (singular noun + faulty inflection)
	objrelpl = """ 
	S -> NP VP
	NP -> Det Npl NPcomp
	NPcomp -> adp Detpl Npl Vpl
	VP -> Vpl
	VP -> Vsi
	Det -> 'in'
	Detpl -> 'de'
	adp -> 'wêrfan'"""

	# within object relative clause (singular noun + faulty inflection)
	objInRel = """ 
	S -> NP VP
	NP -> Det Nsi NPcomp
	NPcomp -> adp Detsi Nsi Vrel
	Vrel -> Vsi
	Vrel -> Vpl
	VP -> Vsi
	adp -> 'wêrfan'
	Det -> 'in'
	Detpl -> 'de'
	"""

	# within object relative clause (plural noun + faulty inflection)
	objInRelpl = """ 
	S -> NP VP
	NP -> Det Nsi NPcomp
	NPcomp -> adp Detsi Npl Vrel
	Vrel -> Vpl
	Vrel -> Vsi
	VP -> Vsi
	adp -> 'wêrfan'
	Det -> 'in'
	Detpl -> 'de'
	"""

if __name__ == '__main__':
	main()