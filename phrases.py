#!/usr/bin/env python
import random
import sys

adverbs =    open( 'adv.txt' ).read().split()
adjectives = open( 'adj.txt' ).read().split()
nouns =      open( 'noun.txt' ).read().split()


phrases = []
for i in range( int( sys.argv[1] ) ) :
    phrase = 'the ' + ' '.join( map( random.choice, [ adverbs, adjectives, nouns ] ) )
    
    if not phrases.__contains__( phrase ) :
        phrases.append(phrase)

for phrase in phrases :
    print phrase
