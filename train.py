import numpy as np
import matplotlib.pyplot as plt
import re, string

debug = False #prolly won't load if file is >50kb

textend = ["<|endoftext|>"]

def findngrams(text):

    global startersresult, pairsresult, tripletsresult, quadrupletsresult, pentupletsresult
    global unique_pairs, frequency, starterwords


    texttuple = text.split() #convert to tuple


    print("Finding Sentence starters...")

    starters = np.array([texttuple[i+1] for i in range(len(texttuple) - 1) if texttuple[i] in textend])
    unique_starters, frequency = np.unique(starters, axis=0, return_counts=True)

    print("Storing Sentence starters...")

    startersresult = [(int(f), a) for f, (a) in zip(frequency, unique_starters) if f > 1]


    #removes ignored strings out of the tuple before processing ngrams
    texttuple = [word for word in texttuple if word not in textend]

    print("Analysing Bigrams...")
    pairs = np.array(list(zip(texttuple[:-1], texttuple[1:])), dtype=[('col1', 'O'), ('col2', 'O')])
    #having the dtype as object is much more memory efficient (aparrently)

    unique_pairs, frequency = np.unique(pairs, axis=0, return_counts=True)

    print("Storing Bigrams...")

    pairsresult = [(int(f), a, b) for f, (a, b) in zip(frequency, unique_pairs) if f > 1]
    #if the pairs only occur once it doesn't make it to the final memory
    #this removes anomalies and improves performance and filesize MASSIVELY

    #TRIPLETS (same thing as pairs just with 3 of them lmao)

    print("Analysing Trigrams...")

    triplets = np.array(list(zip(texttuple[:-2], texttuple[1:-1], texttuple[2:])), dtype=[('col1', 'O'), ('col2', 'O'), ('col3', 'O')])

    unique_triplets, frequency = np.unique(triplets, axis=0, return_counts=True)
    
    print("Storing Trigrams...")

    tripletsresult = [(int(f), a, b, c) for f, (a, b, c) in zip(frequency, unique_triplets) if f > 1]

    #QUADRUPLETS

    print("Analysing Quadragrams...")

    quadruplets = np.array(list(zip(texttuple[:-3], texttuple[1:-2], texttuple[2:-1], texttuple[3:])), dtype=[('col1', 'O'), ('col2', 'O'), ('col3', 'O'), ('col4', 'O')])

    unique_quadruplets, frequency = np.unique(quadruplets, axis=0, return_counts=True)
    
    print("Storing Quadragrams...")

    quadrupletsresult = [(int(f), a, b, c, d) for f, (a, b, c, d) in zip(frequency, unique_quadruplets) if f > 1]

    #PENTUPLETS

    print("Analysing Pentagrams...")

    pentuplets = np.array(list(zip(texttuple[:-4], texttuple[1:-3], texttuple[2:-2], texttuple[3:-1], texttuple[4:])), dtype=[('col1', 'O'), ('col2', 'O'), ('col3', 'O'), ('col4', 'O'), ('col5', 'O')])

    unique_pentuplets, frequency = np.unique(pentuplets, axis=0, return_counts=True)
    
    print("Storing Pentagrams...")

    pentupletsresult = [(int(f), a, b, c, d, e) for f, (a, b, c, d, e) in zip(frequency, unique_pentuplets) if f > 1]

