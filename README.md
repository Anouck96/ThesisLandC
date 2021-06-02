# ThesisLandC

This directory contains all the code for my master thesis *Inside "the Frisian mind" of multilingual language models: The sensitivity of multilingual pre-trained neural language models on Frisian syntax"*.


## Directory agreement
The different programs contain the context free grammars (CFG) for every subphenomenon. It also adds the selected random words for nonce sentences to the CFG. The data is written to separate tsv files. These files can be found in the data directory. The files consist out of the name of the phenomenon, the variant (e.g. if it is nonce or if both nouns are singular) and the minimal pairs. The following subphenomena can be found in the following files:

* simpleAgreement.py: Simple agreement
* sentcomp.py: Agreement in a sentential complement
* shortVP.py: Short verb phrase (VP) coordination
* longVP.py: Long verb phrase (VP) coordination
* prephrase_anim.py: Across a prepositional phrase (animate)
* prephrase_inanim.py: Across a prepositinoal phrase (inanimate)
* subrelclause.py: Across a subject relative clause
* withinobjrel_inanim.py: Within an object relative clause (inanimate)
* acrossobjrel_anim.py: Across an object relative clause (animate)
* acrossobjrel_inanim.py: Across an object relative clause (inanimate)

## Directory npi
The negative polarity items (npi) directory also consists out of the programs that contain the context free grammars. The data is again stored in the data directory. The following phenomena can be found:

* simplenpi_anim.py: Simple npi (animate)
* simplenpi_inanim.py: Simple npi (inanimate)
* npiacrossrel_animate.py: Npi across a relative clause (animate)
* npiacrossrel_inanimate.py: Npi across a relative clause (inanimate)


## Directory reflexive
The reflexive directory also contains the code and the created sentences (in data).

* simpleReflexive.py: Simple reflexive
* reflexiveSentComp.py: Reflexive in a sentential complement
* reflexiveAcrossObjRel.py: Reflexive across an object relative clause

## Directory eval


## getfreqs.py
This program simply counts all the occurences of words in the oersetter corpus and returns a list of the words and the frequency, in descending order.

## selectWords.py
Selects random words based on PoS-tag and/or features from the frisian dictionary (https://taalweb.frl/foarkarswurdlist). The default program selects singular and plural verbs and nouns (same words different inflection), infinitive verbs, proper nouns, adjectives and adpositions and writes these to separate csv files. The default amount is 4 words per category, this can be altered by changing the nr in the code.


