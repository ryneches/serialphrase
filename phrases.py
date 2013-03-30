#!/usr/bin/env python
import random
import sys

# Assing a variable for this namespace
number_of_phrases = 0
try:
    number_of_phrases = int( sys.argv[1] ) 
    if number_of_phrases <= 0:
        # User passed in 0 or negative number
        print("Please pass in a positive number of phrases.")
except IndexError:
    # User didn't pass in a number
    print("Please pass in a number of phrases.")

adverbs =    open( 'adv.txt' ).read().split()
adjectives = open( 'adj.txt' ).read().split()
nouns =      open( 'noun.txt' ).read().split()


phrases = []
for i in range( number_of_phrases ) :
    phrase = 'the ' + ' '.join( map( random.choice, [ adverbs, adjectives, nouns ] ) )
    
    if not phrases.__contains__( phrase ) :
        phrases.append(phrase)

for phrase in phrases :
    print phrase
