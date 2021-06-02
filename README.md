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
The eval directory contains the code needed for testing and evaluating the models. The programs eval_bert.py, eval_roberta.py and eval_xlm.py are used to probe respectively bert-base-multilingual-cased, xlm-roberta-large, and xlm-mlm-100-1280 on the created sentences. If the correct inflection is given a higher probability by these models it will return "True" for this specific minimal pair. If it returns a lower (or the same) probability it will return "False". The file that should be tested should be given in the code itself. When the code is run like: eval_bert.py > results.txt it will write the output to a file. These outputs can be found in the directories evalmBERT, results_RoBERTa_large and results_xlmmlm. With gen_tbl.py scores can be obtained for the total phenomenon or for every variant within this phenomenon. This program takes one of the output files as input and calculates the scores.

The program createBase.py creates a random baseline of 50%. For the number of lines in a file it returns a equal amount of lines with an equal number of "True" and "False" but in a random order.
mcNemartest.py is used for comparing the outputs of two models. It returns the statistic and the p-value and if the null hypothesis should be rejected or not. It can be run as follows: python3 mcNemartest.py resultsmodel1.txt resultsmodel2.txt.

## getfreqs.py
This program simply counts all the occurences of words in the oersetter corpus and returns a list of the words and the frequency, in descending order.

## selectWords.py
Selects random words based on PoS-tag and/or features from the frisian dictionary (https://taalweb.frl/foarkarswurdlist). The default program selects singular and plural verbs and nouns (same words different inflection), infinitive verbs, proper nouns, adjectives and adpositions and writes these to separate csv files. The default amount is 4 words per category, this can be altered by changing the nr in the code.


