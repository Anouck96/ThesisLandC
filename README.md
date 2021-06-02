# ThesisLandC

This directory contains all the code for my master thesis *Inside "the Frisian mind" of multilingual language models: The sensitivity of multilingual pre-trained neural language models on Frisian syntax"*.


## Directory agreement

## Directory npi

## Directory reflexive

## Directory eval


## getfreqs.py
This program simply counts all the occurences of words in the oersetter corpus and returns a list of the words and the frequency, in descending order.

## selectWords.py
Selects random words based on PoS-tag and/or features from the frisian dictionary (https://taalweb.frl/foarkarswurdlist). The default program selects singular and plural verbs and nouns (same words different inflection), infinitive verbs, proper nouns, adjectives and adpositions and writes these to separate csv files. The default amount is 4 words per category, this can be altered by changing the nr in the code.


