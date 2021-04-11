
def main():

	# Simple reflexive (singular noun + faulty inflection)
	refl = """ 
	S -> NP VP ANPHR
	NP -> Det Nsi
	VP -> Vsi
	ANPHR -> ANsi
	ANPHR -> ANpl
	Det -> 'in'
	ANsi -> 'himself'
	ANpl -> 'themselves'"""

	# Simple reflexive (plural noun + faulty inflection)
	reflpl = """ 
	S -> NP VP ANPHR
	NP -> Det Npl
	VP -> Vpl
	ANPHR -> ANpl
	ANPHR -> ANsi
	Det -> 'de'
	ANsi -> 'himself'
	ANpl -> 'themselves'"""

	# Reflexive sentential complement (singular noun + faulty inflection)
	sentRefl = """ 
	S -> NP VPpl Comp
	NP -> Detpl Npl
	VPpl -> Vpl
	Comp -> sconj NP ANPHRsi VPsi
	Comp -> sconj NP ANPHRpl VPsi
	sconj -> 'dat'
	NP -> Det Nsi
	VPsi -> Vsi
	Det -> 'in'
	Detpl -> 'de'
	"""
	# Reflexive sentential complement (plural noun + faulty inflection)
	sentReflpl = """ 
	S -> NP VPsi Comp
	NP -> Det Nsi
	VPpl -> Vpl
	Comp -> sconj NP ANPHRpl VPpl
	Comp -> sconj NP ANPHRsi VPpl
	sconj -> 'dat'
	NP -> Detpl Npl
	VPsi -> Vsi
	Det -> 'in'
	Detpl -> 'de'
	"""

	# Reflexive across object relative clause (singular noun + faulty inflection)
	reflOb = """ 
	S -> NP VP
	NP -> Detsi Nsi RelCl
	RelCl -> adp Detpl Npl Vpl
	VP -> Vsi ANPHRsi
	VP -> Vsi ANPHRpl
	Detsi -> 'in'
	Detpl -> 'de'
	adp -> 'wêrfan'"""

	# Reflexive across object relative clause (singular noun + faulty inflection)
	reflObpl = """ 
	S -> NP VP
	NP -> Detpl Npl RelCl
	RelCl -> adp Detsi Nsi Vsi
	VP -> Vsi ANPHRpl
	VP -> Vsi ANPHRsi
	Detsi -> 'in'
	Detpl -> 'de'
	adp -> 'wêrfan'"""

if __name__ == '__main__':
	main()